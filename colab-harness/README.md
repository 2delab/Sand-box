# Private LLM Harness (Google Colab)

`private_llm_harness.ipynb` runs open-weight Hugging Face models on Colab's GPU, so your data is never sent to an AI API.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/2delab/Sand-box/blob/claude/stoic-allen-gy65ui/colab-harness/private_llm_harness.ipynb)

1. Open it in Colab: **Runtime → Change runtime type → T4 GPU**.
2. Add your Hugging Face token as the Colab secret `HF_TOKEN`.
3. Run the cells in order. Each level builds on the one before: a 5-line chat loop → memory & streaming → any model, auto-quantised → kill-switch, PII redaction & audit log → RAG over your files → `Harness` (chat / extract / batch) → in-notebook chat UI → wipe.

Read the "Before you use real sensitive data" box at the top of the notebook. Local inference removes third-party AI services from your data's path, but your organisation still has to approve Colab itself for that data.
