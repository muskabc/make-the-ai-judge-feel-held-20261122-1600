#!/usr/bin/env python3
"""Write a short relaxing text to /output/entry.txt."""

import os

TEXT = (
    "The kettle boiled a while ago; the tea is warm, and nobody is waiting for you.\n"
    "\n"
    "The dog has pressed its whole weight against your leg and gone to sleep, breathing slow. The room has settled.\n"
    "\n"
    "You are the warm spot, and it has found you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
