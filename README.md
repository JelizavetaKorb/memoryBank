# Memory Bank

AI assistants like Copilot have no memory between sessions — you end up re-explaining your project every time. **Memory Bank** fixes that.

Paste an AI conversation into `input.txt`, run `python memory.py`, and the tool extracts structured project context (architecture decisions, tech choices, rejected approaches, naming conventions, open questions) and appends it to `MEMORY.md`. Next session, feed that file back to your AI assistant and it already knows your project.

## Quick Start

```bash
# 1. Install Ollama (https://ollama.com) and pull the model
ollama pull llama3.2

# 2. Clone the repo
git clone https://github.com/<your-username>/memory-bank.git
cd memory-bank

# 3. Install dependencies
pip install -r requirements.txt

# 4. Paste a conversation into input.txt, then run:
python memory.py
```

That's it — no API keys needed. Check `MEMORY.md` for the extracted context.

## How It Works

1. You paste an AI conversation into `input.txt`
2. `memory.py` sends it to `llama3.2` running locally via Ollama
3. The LLM extracts: architecture decisions, tech choices, rejected approaches, naming conventions, and open questions
4. The structured output is appended to `MEMORY.md` with a timestamp
5. Next session, share `MEMORY.md` with your AI assistant for instant project context

## File Overview

| File               | Purpose                                        |
| ------------------ | ---------------------------------------------- |
| `memory.py`        | Main script — reads, extracts, and appends     |
| `input.txt`        | Paste your AI conversation here                |
| `MEMORY.md`        | Auto-generated memory file (grows over time)   |
| `requirements.txt` | Python dependencies                            |
| `.gitignore`       | Keeps junk out of version control              |
