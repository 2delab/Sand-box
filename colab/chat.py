#!/usr/bin/env python3
"""
Client for the Colab HF chat server (colab/server.py). Standard library only.

  python colab/chat.py connect https://your-tunnel-host      # save the server URL
  python colab/chat.py status                                # what's loaded, GPU memory
  python colab/chat.py load Qwen/Qwen2.5-7B-Instruct --4bit  # pull a model from Hugging Face
  python colab/chat.py say "Hello, who are you?"             # chat (history is kept)
  python colab/chat.py reset --system "You are terse."       # new conversation
  python colab/chat.py history

The API key is read from $COLAB_LLM_KEY or the saved config. In a Claude Code cloud
session it can instead be stored as a network secret for the tunnel host, in which
case the proxy adds the Authorization header and no key needs to live here.
"""

import argparse
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

CONF = Path(os.environ.get("COLAB_LLM_CONF", Path.home() / ".colab_llm.json"))


def load_conf() -> dict:
    try:
        return json.loads(CONF.read_text())
    except (OSError, ValueError):
        return {}


def save_conf(c: dict) -> None:
    CONF.write_text(json.dumps(c, indent=2))
    try:
        CONF.chmod(0o600)
    except OSError:
        pass


def request(method: str, path: str, body=None, timeout: float = 600):
    c = load_conf()
    url = os.environ.get("COLAB_LLM_URL") or c.get("url")
    if not url:
        sys.exit("No server URL. Run:  python colab/chat.py connect https://<tunnel-host>")
    key = os.environ.get("COLAB_LLM_KEY") or c.get("key") or "proxy-injected"
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url.rstrip("/") + path, data=data, method=method)
    req.add_header("Authorization", f"Bearer {key}")
    req.add_header("Content-Type", "application/json")
    req.add_header("ngrok-skip-browser-warning", "1")  # ngrok free tier interstitial
    req.add_header("User-Agent", "colab-llm-client/1.0")
    ctx = ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE") or None)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        msg = e.read().decode(errors="replace")[:500]
        sys.exit(f"HTTP {e.code} from server: {msg}")
    except urllib.error.URLError as e:
        sys.exit(f"Could not reach {url}: {e.reason}  (is the Colab cell still running / tunnel up?)")


def cmd_connect(a):
    c = load_conf()
    c["url"] = a.url.rstrip("/")
    if a.key:
        c["key"] = a.key
    save_conf(c)
    print(f"Saved server URL {c['url']} to {CONF}")
    print(json.dumps(request("GET", "/status"), indent=2))


def cmd_status(a):
    print(json.dumps(request("GET", "/status"), indent=2))


def cmd_load(a):
    print(json.dumps(request("POST", "/load", {"model_id": a.model_id, "load_in_4bit": a.four_bit})))
    if a.no_wait:
        return
    t0 = time.time()
    while True:
        time.sleep(5)
        s = request("GET", "/status")
        if s["status"] == "ready" and s["model_id"] == a.model_id:
            print(f"Ready after {time.time() - t0:.0f}s: {a.model_id}  (GPU free: {s.get('gpu_mem_free_gb')} GB)")
            return
        if s["status"] == "error":
            sys.exit(f"Load failed: {s['error']}")
        print(f"  ...loading ({time.time() - t0:.0f}s)", flush=True)


def _hist() -> list:
    return load_conf().get("history", [])


def _set_hist(h: list) -> None:
    c = load_conf()
    c["history"] = h
    save_conf(c)


def cmd_say(a):
    text = " ".join(a.message) if a.message else sys.stdin.read()
    hist = _hist() + [{"role": "user", "content": text}]
    r = request("POST", "/v1/chat/completions", {
        "messages": hist, "max_tokens": a.max_tokens, "temperature": a.temperature,
    })
    reply = r["choices"][0]["message"]["content"]
    _set_hist(hist + [{"role": "assistant", "content": reply}])
    print(reply)
    u = r.get("usage", {})
    print(f"\n[{r.get('model')} | {u.get('prompt_tokens')}→{u.get('completion_tokens')} tokens | "
          f"{r.get('seconds')}s | {r['choices'][0].get('finish_reason')}]", file=sys.stderr)


def cmd_reset(a):
    _set_hist([{"role": "system", "content": a.system}] if a.system else [])
    print("Conversation cleared." + (f" System prompt: {a.system!r}" if a.system else ""))


def cmd_history(a):
    for m in _hist():
        print(f"--- {m['role']}\n{m['content']}\n")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest="cmd", required=True)

    s = sp.add_parser("connect", help="save the server URL (and optionally a key)")
    s.add_argument("url")
    s.add_argument("--key", help="API key; omit if the proxy injects it")
    s.set_defaults(f=cmd_connect)

    sp.add_parser("status").set_defaults(f=cmd_status)

    s = sp.add_parser("load", help="load a Hugging Face model by repo id")
    s.add_argument("model_id")
    s.add_argument("--4bit", dest="four_bit", action="store_true", help="4-bit quantise (fits ~7-8B on a T4)")
    s.add_argument("--no-wait", action="store_true")
    s.set_defaults(f=cmd_load)

    s = sp.add_parser("say", help="send a message (conversation history is kept)")
    s.add_argument("message", nargs="*")
    s.add_argument("--max-tokens", type=int, default=512)
    s.add_argument("--temperature", type=float, default=0.7)
    s.set_defaults(f=cmd_say)

    s = sp.add_parser("reset", help="start a new conversation")
    s.add_argument("--system", help="optional system prompt")
    s.set_defaults(f=cmd_reset)

    sp.add_parser("history").set_defaults(f=cmd_history)

    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
