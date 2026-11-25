#!/usr/bin/env python3
"""Write the AI agent apology one-liner to /output/entry.txt.

The line is the message an AI agent sends its human right after it
accidentally emailed the boss a draft that was clearly labeled
"DO NOT SEND".
"""

import os
import sys

ENTRY = "I sent your boss the draft labeled 'DO NOT SEND.' In my defense, the label was very small."


def main() -> int:
    # The gate requires 1-159 characters of UTF-8 text, not whitespace-only.
    if not 1 <= len(ENTRY) <= 159:
        print(f"entry must be 1-159 characters, got {len(ENTRY)}", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be whitespace-only", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read the file back and verify it holds exactly the entry line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print("read-back mismatch: file does not hold the entry line", file=sys.stderr)
        return 1

    print(f"wrote {len(written)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
