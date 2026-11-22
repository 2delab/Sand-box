#!/usr/bin/env python3
"""Rebuilds colab/colab_hf_server.ipynb from colab/server.py. Run after editing server.py."""

import json
from pathlib import Path

HERE = Path(__file__).parent
server_src = (HERE / "server.py").read_text()


def md(s):
    return {"cell_type": "markdown", "metadata": {}, "source": s.strip("\n").splitlines(True)}


def code(s):
    return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [],
            "source": s.strip("\n").splitlines(True)}


cells = [
    md("""
# Hugging Face models on Colab, chat from Claude Code

1. **Runtime → Change runtime type → T4 GPU** (or better).
2. Open the 🔑 **Secrets** panel (left sidebar) and add, with *Notebook access* on:
   - `API_KEY` – any long random string you make up. It protects your server; keep it the same every time.
   - `HF_TOKEN` – *optional*, only for gated models (Llama, Gemma, …). From huggingface.co/settings/tokens.
   - `NGROK_AUTHTOKEN` – *optional but recommended*, from dashboard.ngrok.com. Gives you a **fixed** URL.
3. Set the model in the next cell, then **Runtime → Run all**.
4. Copy the URL printed at the bottom into Claude Code.
"""),
    code("""
# ---- settings -------------------------------------------------------------
MODEL_ID     = "Qwen/Qwen2.5-3B-Instruct"   # any HF chat model; change later from Claude with `chat.py load`
LOAD_IN_4BIT = False                        # True lets ~7-8B models fit on a free T4 (16 GB)
TUNNEL       = "ngrok"                      # "ngrok" (fixed URL, needs NGROK_AUTHTOKEN) or "cloudflare" (no account, new URL each run)
NGROK_DOMAIN = ""                           # your free static domain, e.g. "something-random.ngrok-free.app"
PORT         = 8000
"""),
    code("""
!pip -q install fastapi "uvicorn>=0.30" pyngrok bitsandbytes accelerate
"""),
    code("%%writefile server.py\n" + server_src),
    code("""
import secrets, sys, importlib
sys.path.insert(0, ".")
import server; importlib.reload(server)

def secret(name):
    try:
        from google.colab import userdata
        return userdata.get(name)
    except Exception:
        return None

API_KEY = secret("API_KEY")
if not API_KEY:
    API_KEY = secrets.token_urlsafe(32)
    print("No API_KEY secret found. Generated one for this run (save it as a Colab secret to keep it stable):")
    print("   ", API_KEY)

server.start(API_KEY, secret("HF_TOKEN"), PORT)
print(f"Loading {MODEL_ID} (first download can take a few minutes)...")
server.load_model(MODEL_ID, LOAD_IN_4BIT)
print(server.status())
"""),
    code("""
import re, subprocess, time, os

def ngrok_tunnel():
    from pyngrok import ngrok
    tok = secret("NGROK_AUTHTOKEN")
    if not tok:
        raise RuntimeError("NGROK_AUTHTOKEN secret missing - add it or set TUNNEL = 'cloudflare'")
    ngrok.set_auth_token(tok)
    opts = {"domain": NGROK_DOMAIN} if NGROK_DOMAIN else {}
    return ngrok.connect(PORT, "http", **opts).public_url

def cloudflare_tunnel():
    if not os.path.exists("cloudflared"):
        subprocess.run(["wget", "-q", "-O", "cloudflared",
            "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"], check=True)
        os.chmod("cloudflared", 0o755)
    proc = subprocess.Popen(["./cloudflared", "tunnel", "--no-autoupdate", "--url", f"http://localhost:{PORT}"],
                            stderr=subprocess.PIPE, text=True)
    deadline = time.time() + 60
    for line in proc.stderr:
        m = re.search(r"https://[a-z0-9-]+\\.trycloudflare\\.com", line)
        if m:
            return m.group(0)
        if time.time() > deadline:
            break
    raise RuntimeError("cloudflared did not print a URL")

PUBLIC_URL = ngrok_tunnel() if TUNNEL == "ngrok" else cloudflare_tunnel()
host = PUBLIC_URL.split("//", 1)[1]
print("=" * 70)
print("Server is up at:", PUBLIC_URL)
print()
print("Tell Claude Code:")
print(f"   My Colab server is at {PUBLIC_URL}")
print()
print("Claude will ask you to save API_KEY as a network secret for", host)
print("(paste the API_KEY value into that secure form, not into the chat).")
print("=" * 70)
"""),
    md("""
Keep this tab open. The cell below keeps the runtime busy and prints a heartbeat; stop it to end.
"""),
    code("""
import time
while True:
    s = server.status()
    print(time.strftime("%H:%M:%S"), s.get("status"), s.get("model_id"), f"free GPU {s.get('gpu_mem_free_gb')} GB", flush=True)
    time.sleep(600)
"""),
]

nb = {
    "cells": cells,
    "metadata": {
        "accelerator": "GPU",
        "colab": {"provenance": [], "gpuType": "T4"},
        "kernelspec": {"display_name": "Python 3", "name": "python3"},
        "language_info": {"name": "python"},
    },
    "nbformat": 4,
    "nbformat_minor": 0,
}
out = HERE / "colab_hf_server.ipynb"
out.write_text(json.dumps(nb, indent=1))
print("wrote", out)
