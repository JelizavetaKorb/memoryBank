# memory.py — Main script for Memory Bank
# Reads input.txt, sends it to an LLM, and appends a summary to MEMORY.md

import os
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
MEMORY_FILE = SCRIPT_DIR / "MEMORY.md"

SYSTEM_PROMPT = (
    "You are a memory-bank assistant. The user will paste a developer conversation. "
    "Extract the key decisions, facts, code snippets, and action items. "
    "Return a concise Markdown summary suitable for appending to a long-running MEMORY.md file."
)


def read_input() -> str:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"{INPUT_FILE} not found. Paste your conversation there first.")
    text = INPUT_FILE.read_text().strip()
    if not text:
        raise ValueError("input.txt is empty. Paste a conversation and try again.")
    return text


def summarize(conversation: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY is not set. Add it to .env")

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": conversation},
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content


def append_to_memory(summary: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n---\n\n## {timestamp}\n\n{summary}\n"
    with open(MEMORY_FILE, "a") as f:
        f.write(entry)
    print(f"✅ Memory updated — see {MEMORY_FILE}")


def main() -> None:
    conversation = read_input()
    print("🧠 Summarising conversation …")
    summary = summarize(conversation)
    append_to_memory(summary)


if __name__ == "__main__":
    main()
