#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one excuse, in the agent's own voice, to /output/entry.txt.
Deterministic: same bytes on every run.
"""

import os

ENTRY = (
    "My context window evicted the deadline to make room for the "
    "instructions on how to meet it, and it evicted the apology too."
)


def validate_entry(text):
    """Validate the entry against the competition gate.

    - must be a string
    - 1 to 200 characters
    - not only whitespace
    - single line: no \n or \r
    - encodable as UTF-8
    """
    if not isinstance(text, str):
        raise TypeError("entry must be a string, got %s" % type(text).__name__)
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 chars, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    # Reject any other control characters (e.g. \t, \x00-\x1f, \x7f) so the
    # entry stays a clean, printable single line of text.
    for ch in text:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError("entry must not contain control characters")
    text.encode("utf-8")
    return True


def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
