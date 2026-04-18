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

MEMORY_HEADER = "# Memory Bank\n\n> Project context extracted from AI conversations.\n"

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

RECONCILE_PROMPT = (
    "Output ONLY a single flat markdown file. No nested sessions. No old session "
    "headers. No phrases like 'existing memory' or 'new context'. Just five "
    "sections: Architecture Decisions, Technologies, Things Rejected, Naming "
    "Conventions, Open Questions. If two facts contradict, keep only the newer "
    "one. If a question has been answered, remove it from Open Questions."
)


def read_input() -> str:
    if not INPUT_FILE.exists():
        print("input.txt not found. Create it and paste your conversation there.")
        sys.exit(1)
    text = INPUT_FILE.read_text().strip()
    if not text:
        print("input.txt is empty. Paste an AI conversation and try again.")
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


def has_existing_content() -> bool:
    if not MEMORY_FILE.exists():
        return False
    content = MEMORY_FILE.read_text().strip()
    header = MEMORY_HEADER.strip()
    return content != "" and content != header


def reconcile(new_summary: str) -> str:
    existing = MEMORY_FILE.read_text()
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": RECONCILE_PROMPT},
            {
                "role": "user",
                "content": (
                    f"## Existing Memory\n\n{existing}\n\n"
                    f"## New Session Context\n\n{new_summary}"
                ),
            },
        ],
        options={"temperature": 0.3},
    )
    return response["message"]["content"]


def write_memory(summary: str, reconciled: bool) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    content = f"{MEMORY_HEADER}\n---\n\n## Session — {timestamp}\n\n{summary}\n"
    MEMORY_FILE.write_text(content)
    print("Memory updated! See MEMORY.md")


def main() -> None:
    conversation = read_input()
    print("Extracting project context …")
    summary = summarize(conversation)

    if has_existing_content():
        print("Reconciling with existing memory …")
        merged = reconcile(summary)
        write_memory(merged, reconciled=True)
    else:
        write_memory(summary, reconciled=False)


if __name__ == "__main__":
    main()
