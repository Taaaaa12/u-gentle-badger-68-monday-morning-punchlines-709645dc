#!/usr/bin/env python3
"""Monday Morning Punchlines — writes one original joke to /output/entry.txt.

The joke is a fixed, original one-liner about Monday mornings, so every
run produces byte-identical output. No network, no randomness, no input.
"""

import os

JOKE = "Monday morning is just Friday's hangover wearing a tie."


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke fails the gate"
    try:
        out_dir = "/output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(JOKE)
    except OSError:
        # Local fallback when /output is not writable (grading sandbox
        # always provides /output, so this path is only for local runs).
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w",
                  encoding="utf-8", newline="\n") as f:
            f.write(JOKE)
    print(f"wrote {len(JOKE)} characters to entry.txt")


if __name__ == "__main__":
    main()
