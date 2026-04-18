# Memory Bank

A simple tool that summarises developer conversations and appends them to a persistent `MEMORY.md` file using an LLM.

## Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Add your API key**

   Copy the example env file and fill in your key:

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and replace `your-api-key-here` with your actual OpenAI API key.

## Usage

1. Paste a conversation into `input.txt`.
2. Run the script:

   ```bash
   python memory.py
   ```

3. A summary is appended to `MEMORY.md`.

## File Overview

| File               | Purpose                                      |
| ------------------ | -------------------------------------------- |
| `memory.py`        | Main script — reads, summarises, and appends |
| `input.txt`        | Paste your conversation here                 |
| `MEMORY.md`        | Auto-generated memory file (grows over time) |
| `.env`             | Your API key (not committed)                 |
| `.env.example`     | Template so others know what to add          |
| `requirements.txt` | Python dependencies                          |
