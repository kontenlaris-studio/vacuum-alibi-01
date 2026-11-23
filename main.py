#!/usr/bin/env python3
"""The Vacuum's Alibi — writes one alibi line (<=200 chars) to /output/entry.txt.

Stdlib only. Deterministic: the same line every run.
"""

import os

LINE = "At the time of the missing sock, I was under the couch, as always. Ask the dust bunnies — they saw everything. I saw nothing. I am innocent."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
