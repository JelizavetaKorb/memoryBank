# Memory Bank

Give your AI assistant a long-term memory. Paste a conversation, run one command, and your project context is saved forever.

## The Problem

AI assistants have no memory between sessions. Every new chat starts from zero. You waste time re-explaining your architecture, your tech stack, and the decisions you already made.

## How It Works

1. Paste your AI conversation into `input.txt`
2. Run `python memory.py`
3. Your `MEMORY.md` updates automatically

## Quick Start

### Minimal Setup (one file)

1. Download `memory.py` and drop it into your project folder
2. Install [Ollama](https://ollama.com)
3. Run `ollama pull llama3.2`
4. Paste your AI conversation into `input.txt`
5. Run `python memory.py`
6. Before each next prompt write "Read MEMORY.md for context..." 

That's it. No config, no accounts, no API keys.


## Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed locally

## What Gets Extracted

- Architecture decisions
- Technologies chosen and why
- Things tried and rejected
- Naming conventions
- Open questions

## Roadmap

- **v1** Python script (acomplished)
- **v2** `pip` package — one-line install anywhere
- **v3** VS Code extension — right-click any conversation to save
