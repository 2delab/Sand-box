# 🔒 Private LLM Harness for Google Colab

One notebook, `private_llm_harness.ipynb`, that runs open-weight models from Hugging Face **on Colab's own GPU**. Your text and files are processed on that machine and are never sent to an AI API (OpenAI, Anthropic, Gemini, Hugging Face Inference…). It starts with a 5-line chat loop and builds, one cell at a time, to a full harness with privacy guardrails. It's written for beginners and experts alike.

```
Hugging Face ──(model weights only)──▶  Colab VM + GPU  ◀── your files
                                          model, data, logs stay here
                                          deleted when you delete the runtime
```

## Quick start
1. **Open the notebook in Colab:** go to [colab.research.google.com](https://colab.research.google.com), choose **File → Upload notebook**, and select `private_llm_harness.ipynb`.
2. **Pick a GPU:** **Runtime → Change runtime type → T4 GPU** (free) or L4/A100 (paid).
3. **Add your token:** create a **Read** token at [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens). In Colab, click 🔑 **Secrets** in the left bar, add `HF_TOKEN` and switch on *Notebook access*. The default Qwen models are public, so this step is optional for them.
4. **Protect your outputs:** **Edit → Notebook settings → tick "Omit code cell output when saving this notebook"**.
5. **Run the cells in order** (Shift+Enter). Each one ends with ✅ when it worked. When an input box appears, press Enter on an empty box to continue.

## What's inside
| Level | You get | Key idea |
|---|---|---|
| 0 · Setup | GPU check, installs, login | Token read from Colab Secrets, never written in code |
| 1 · Chat loop | A working chatbot in 5 lines | `pipeline` = model + tokenizer |
| 2 · Real chat | Memory, system prompt, streaming | Models are stateless; you resend the whole history each turn |
| 3 · Any model | Dropdown or any HF model ID | Auto 4-bit if it won't fit; safetensors only; revision pinned |
| 4 · Guardrails | Network kill-switch, PII redaction, audit log | Protection against accidents, not just good intentions |
| 5 · Your documents | Cited Q&A over PDF/DOCX/TXT/CSV (RAG) | Local embeddings; PII removed before indexing |
| 6 · Harness | `h.chat()`, `h.extract()`, `h.batch()` | Every call: redact → generate → restore → audit |
| 7 · Chat app | Chat window inside the notebook | No public link, unlike Gradio `share=True` or ngrok |
| 8 · Cleanup | Wipe data, free GPU, log out | Then delete the runtime |

### Harness in 4 lines
```python
h.chat("Summarise our leave policy", use_docs=True)        # cited answer from your files
h.extract(email_text, {"name": "sender", "amount": "£"})   # → dict, retries until valid JSON
h.batch(df.text.tolist(), "Classify: billing, bug or other")  # fast batched GPU jobs
h.reset()                                                   # new conversation
```

## Privacy model
| Layer | What it does | Limit |
|---|---|---|
| Local inference | Model runs on the Colab VM, so no AI API is called | Colab is still Google infrastructure |
| Network kill-switch | Blocks outbound connections from the notebook's Python process after models are downloaded, including through local proxies | Doesn't cover `!shell` commands |
| PII redaction | Emails, phones, cards, IBANs, SSNs, UK NI numbers, postcodes, IPs and names become `[EMAIL_1]`-style placeholders before the model sees them; real values are restored in the answer | Not perfect, so add your own identifiers to `PII_PATTERNS` |
| Audit log | `audit.jsonl`: time, model, revision, prompt hash, tokens, duration | Stores no text unless `LOG_CONTENT=True` |
| Security defaults | `use_safetensors=True`, `trust_remote_code=False`, pinned revision | Only use models from sources you trust |
| Cleanup | Clears the redaction map, deletes the workspace, logs out | You still need to delete the runtime and clear outputs |

### ⚠️ Compliance: read before using real data
This notebook **removes third-party AI services from your data's path**. It doesn't make Colab itself approved for your data.
- Check that your organisation permits Colab for this data class. **Consumer Colab isn't covered by agreements such as a HIPAA BAA.**
- For regulated data, use **Colab Enterprise** or your own GPU server. The code runs on any Jupyter machine with a GPU, and Colab-only parts fall back automatically.
- Test with the built-in synthetic data first. Always finish with Level 8, then **Runtime → Disconnect and delete runtime**.

## Hardware guide
| Runtime | Comfortable model size |
|---|---|
| T4 (free, 15 GB) | 1.5–3B full precision, 7–8B in 4-bit |
| L4 (24 GB) / A100 (40–80 GB) | 7–8B full precision, 14–32B in 4-bit |
| TPU / CPU | ≤3B, slow. TPU is experimental: the first tokens take minutes while it compiles. |

## Troubleshooting
| Symptom | Fix |
|---|---|
| `CUDA out of memory` | Smaller model, `QUANTIZE="4bit"`, or a lower `max_new_tokens`. Then restart the session. |
| `401` / `403` / gated repo | Accept the licence on the model page. Check the secret name `HF_TOKEN` and that *Notebook access* is on. |
| `🔒 Blocked by privacy kill-switch` | Intended. Download inside `with network_allowed():`. |
| Rambling answers | Use an *Instruct* / *-it* model and lower `temperature`. |
| Very slow | Check that cell 0.1 reports **GPU**. |

## Going further
vLLM for 5–20× faster batch jobs · `outlines`/`xgrammar` for guaranteed JSON · Microsoft Presidio for richer redaction · LoRA fine-tuning with `peft` + `trl` · Colab Enterprise for VPC Service Controls and customer-managed keys.

## Status
Every cell was run end-to-end with small stand-in models on CPU. It hasn't yet been tested on a live Colab GPU with real Hugging Face models. Please report anything that breaks.
