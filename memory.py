"""
memory.py — Memory Bank

Reads a pasted AI conversation from input.txt, extracts structured project
context via Ollama (local), and appends it to MEMORY.md so your AI assistant
can pick up where it left off next session.
"""

import sys
from datetime import datetime
from pathlib import Path

import ollama

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = SCRIPT_DIR / "input.txt"
MEMORY_FILE = SCRIPT_DIR / "MEMORY.md"

SYSTEM_PROMPT = (
    "You are a developer memory assistant. From this AI conversation, extract "
    "and structure the following: "
    "1) Architecture decisions made, "
    "2) Technologies chosen and why, "
    "3) Things tried and rejected and why, "
    "4) Naming conventions established, "
    "5) Open questions remaining. "
    "Format everything as clean markdown with clear section headers. "
    "Be concise and factual."
)


def read_input() -> str:
    if not INPUT_FILE.exists():
        print("❌ input.txt not found. Create it and paste your conversation there.")
        sys.exit(1)
    text = INPUT_FILE.read_text().strip()
    if not text:
        print("⚠️  input.txt is empty. Paste an AI conversation and try again.")
        sys.exit(1)
    return text


def summarize(conversation: str) -> str:
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": conversation},
        ],
        options={"temperature": 0.3},
    )
    return response["message"]["content"]


def append_to_memory(summary: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"\n---\n\n## Session — {timestamp}\n\n{summary}\n"

    if not MEMORY_FILE.exists():
        MEMORY_FILE.write_text("# Memory Bank\n\n> Project context extracted from AI conversations.\n")

    with open(MEMORY_FILE, "a") as f:
        f.write(entry)

    print(f"✅ Memory updated — see MEMORY.md")


def main() -> None:
    conversation = read_input()
    print("🧠 Extracting project context …")
    summary = summarize(conversation)
    append_to_memory(summary)


if __name__ == "__main__":
    main()
