# Chat with Hugging Face models on Google Colab from Claude Code

```
 Claude Code (this chat) ──chat.py──▶ tunnel (ngrok / cloudflare) ──▶ Colab GPU: server.py + transformers
```

| File | Runs on | What it does |
|---|---|---|
| `colab_hf_server.ipynb` | Colab | Downloads a HF model, serves it over an OpenAI-style API, opens a public tunnel |
| `server.py` | Colab | The server itself (the notebook embeds it) |
| `chat.py` | Claude Code | Stdlib-only client: `connect`, `status`, `load`, `say`, `reset`, `history` |
| `build_notebook.py` | anywhere | Regenerates the notebook after you edit `server.py` |

## Setup (once)

1. Open `colab_hf_server.ipynb` in Colab (File → Upload notebook, or open it from GitHub).
2. Runtime → Change runtime type → **T4 GPU**.
3. In Colab's 🔑 Secrets panel add `API_KEY` (any long random string), and optionally
   `HF_TOKEN` (gated models) and `NGROK_AUTHTOKEN` (for a fixed URL; claim a free static
   domain at dashboard.ngrok.com and put it in `NGROK_DOMAIN`).
4. Run all. Copy the URL printed at the end and give it to Claude.

## In Claude Code

Claude saves `API_KEY` as a network secret for the tunnel host, so the key never goes in the chat.
After that:

```bash
python colab/chat.py connect https://<your-host>
python colab/chat.py load mistralai/Mistral-7B-Instruct-v0.3 --4bit
python colab/chat.py say "Explain LoRA in two sentences"
python colab/chat.py reset --system "You are a pirate."
```

With a fixed ngrok domain this only needs doing once. A cloudflare quick tunnel gets a new
hostname every run, so the network secret has to be saved again each time.

## What fits on a free T4 (16 GB)

- Up to about 4B parameters in fp16: Qwen2.5-3B-Instruct, Phi-3.5-mini, Llama-3.2-3B-Instruct
- 7–8B models with `--4bit`: Qwen2.5-7B-Instruct, Mistral-7B-Instruct, Llama-3.1-8B-Instruct
