"""
Tiny OpenAI-compatible chat server for any Hugging Face model, made to run on Google Colab.

Endpoints (all need  Authorization: Bearer <API_KEY>):
  GET  /status                 -> what is loaded / loading, GPU info
  GET  /v1/models              -> the loaded model, OpenAI style
  POST /load                   -> {"model_id": "...", "load_in_4bit": false}  (loads in the background)
  POST /v1/chat/completions    -> OpenAI-style chat request, non-streaming

The notebook writes this file to disk, imports it and calls `start(...)`.
"""

import gc
import secrets
import threading
import time
import traceback
import uuid
from typing import Any, List, Optional, Union

from fastapi import Depends, FastAPI, Header, HTTPException
from pydantic import BaseModel

API_KEY = ""
HF_TOKEN: Optional[str] = None

STATE: dict = {
    "model_id": None,
    "model": None,
    "tokenizer": None,
    "status": "empty",  # empty | loading | ready | error
    "error": None,
    "loading_id": None,
    "load_in_4bit": False,
}
_LOAD_LOCK = threading.Lock()
_GEN_LOCK = threading.Lock()

app = FastAPI(title="Colab HF chat server")


# --------------------------------------------------------------------------- auth
def require_key(authorization: str = Header(default="")) -> None:
    token = authorization.removeprefix("Bearer ").strip()
    if not API_KEY or not secrets.compare_digest(token, API_KEY):
        raise HTTPException(status_code=401, detail="bad or missing API key")


# --------------------------------------------------------------------------- loading
def _dtype_kwarg():
    import torch
    import transformers
    from packaging import version

    if torch.cuda.is_available():
        dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
    else:
        dtype = torch.float32
    key = "dtype" if version.parse(transformers.__version__) >= version.parse("4.56") else "torch_dtype"
    return {key: dtype}


def _unload() -> None:
    STATE["model"] = None
    STATE["tokenizer"] = None
    STATE["model_id"] = None
    gc.collect()
    try:
        import torch

        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    except Exception:
        pass


def load_model(model_id: str, load_in_4bit: bool = False) -> None:
    """Blocking load. Replaces whatever model is loaded."""
    from transformers import AutoModelForCausalLM, AutoTokenizer

    with _LOAD_LOCK, _GEN_LOCK:
        STATE.update(status="loading", loading_id=model_id, error=None)
        try:
            _unload()
            kwargs: dict = {"device_map": "auto", "token": HF_TOKEN}
            if load_in_4bit:
                import torch
                from transformers import BitsAndBytesConfig

                kwargs["quantization_config"] = BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_compute_dtype=torch.float16,
                )
            else:
                kwargs.update(_dtype_kwarg())
            tok = AutoTokenizer.from_pretrained(model_id, token=HF_TOKEN)
            model = AutoModelForCausalLM.from_pretrained(model_id, **kwargs)
            model.eval()
            STATE.update(
                model=model, tokenizer=tok, model_id=model_id, status="ready",
                loading_id=None, load_in_4bit=load_in_4bit,
            )
            print(f"[server] loaded {model_id} (4bit={load_in_4bit})")
        except Exception as e:  # keep the server alive, report the error
            _unload()
            STATE.update(status="error", error=f"{type(e).__name__}: {e}", loading_id=None)
            traceback.print_exc()


def load_model_async(model_id: str, load_in_4bit: bool = False) -> None:
    threading.Thread(target=load_model, args=(model_id, load_in_4bit), daemon=True).start()


# --------------------------------------------------------------------------- generation
def _text(content: Union[str, List[Any], None]) -> str:
    if content is None:
        return ""
    if isinstance(content, str):
        return content
    parts = []
    for p in content:  # OpenAI "content parts"
        if isinstance(p, dict) and p.get("type") == "text":
            parts.append(p.get("text", ""))
    return "\n".join(parts)


def _prompt_ids(tok, messages: List[dict]):
    """Apply the model's chat template, with fallbacks for models that lack one
    or that reject a system message."""
    if getattr(tok, "chat_template", None):
        try:
            return tok.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
        except Exception:
            # Some templates (e.g. older Gemma) refuse a system role: fold it into the first user turn.
            sys_txt = "\n".join(m["content"] for m in messages if m["role"] == "system")
            rest = [dict(m) for m in messages if m["role"] != "system"]
            if sys_txt and rest:
                rest[0]["content"] = sys_txt + "\n\n" + rest[0]["content"]
            return tok.apply_chat_template(rest, add_generation_prompt=True, return_tensors="pt")
    # Base model with no template: plain transcript.
    text = "".join(f"{m['role'].capitalize()}: {m['content']}\n" for m in messages) + "Assistant:"
    return tok(text, return_tensors="pt").input_ids


def generate(messages: List[dict], max_tokens: int, temperature: float, top_p: float):
    import torch

    tok, model = STATE["tokenizer"], STATE["model"]
    ids = _prompt_ids(tok, messages)
    if not torch.is_tensor(ids):  # newer transformers may return a BatchEncoding
        ids = ids["input_ids"]
    ids = ids.to(model.device)
    gen_kwargs = dict(
        max_new_tokens=max_tokens,
        attention_mask=torch.ones_like(ids),
        pad_token_id=tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id,
    )
    if temperature and temperature > 0:
        gen_kwargs.update(do_sample=True, temperature=temperature, top_p=top_p)
    else:
        gen_kwargs.update(do_sample=False)
    with torch.inference_mode():
        out = model.generate(ids, **gen_kwargs)
    new = out[0][ids.shape[-1]:]
    text = tok.decode(new, skip_special_tokens=True).strip()
    finish = "length" if len(new) >= max_tokens else "stop"
    return text, ids.shape[-1], len(new), finish


# --------------------------------------------------------------------------- API
class Msg(BaseModel):
    role: str
    content: Union[str, List[Any], None] = ""


class ChatReq(BaseModel):
    messages: List[Msg]
    model: Optional[str] = None
    max_tokens: int = 512
    temperature: float = 0.7
    top_p: float = 0.95


class LoadReq(BaseModel):
    model_id: str
    load_in_4bit: bool = False


@app.get("/status", dependencies=[Depends(require_key)])
def status():
    info = {k: STATE[k] for k in ("status", "model_id", "loading_id", "error", "load_in_4bit")}
    try:
        import torch

        if torch.cuda.is_available():
            free, total = torch.cuda.mem_get_info()
            info["gpu"] = torch.cuda.get_device_name(0)
            info["gpu_mem_free_gb"] = round(free / 1e9, 2)
            info["gpu_mem_total_gb"] = round(total / 1e9, 2)
        else:
            info["gpu"] = None
    except Exception:
        pass
    return info


@app.get("/v1/models", dependencies=[Depends(require_key)])
def models():
    data = [{"id": STATE["model_id"], "object": "model", "owned_by": "huggingface"}] if STATE["model_id"] else []
    return {"object": "list", "data": data}


@app.post("/load", dependencies=[Depends(require_key)], status_code=202)
def load(req: LoadReq):
    if STATE["status"] == "loading":
        raise HTTPException(409, f"already loading {STATE['loading_id']}")
    load_model_async(req.model_id, req.load_in_4bit)
    return {"status": "loading", "model_id": req.model_id}


@app.post("/v1/chat/completions", dependencies=[Depends(require_key)])
def chat(req: ChatReq):  # plain def -> FastAPI runs it in a worker thread
    if STATE["status"] != "ready":
        raise HTTPException(503, f"no model ready (status={STATE['status']}, error={STATE['error']})")
    msgs = [{"role": m.role, "content": _text(m.content)} for m in req.messages]
    t0 = time.time()
    with _GEN_LOCK:
        text, n_in, n_out, finish = generate(msgs, req.max_tokens, req.temperature, req.top_p)
    return {
        "id": "chatcmpl-" + uuid.uuid4().hex[:24],
        "object": "chat.completion",
        "created": int(t0),
        "model": STATE["model_id"],
        "choices": [{"index": 0, "message": {"role": "assistant", "content": text}, "finish_reason": finish}],
        "usage": {"prompt_tokens": n_in, "completion_tokens": n_out, "total_tokens": n_in + n_out},
        "seconds": round(time.time() - t0, 2),
    }


# --------------------------------------------------------------------------- startup
def start(api_key: str, hf_token: Optional[str] = None, port: int = 8000) -> threading.Thread:
    """Start uvicorn in a background thread (so the Colab cell returns)."""
    import uvicorn

    global API_KEY, HF_TOKEN
    API_KEY, HF_TOKEN = api_key, hf_token or None
    server = uvicorn.Server(uvicorn.Config(app, host="0.0.0.0", port=port, log_level="warning"))
    th = threading.Thread(target=server.run, daemon=True)
    th.start()
    for _ in range(50):
        if server.started:
            break
        time.sleep(0.1)
    print(f"[server] listening on :{port}")
    return th
