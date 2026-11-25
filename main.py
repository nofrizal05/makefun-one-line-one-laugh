"""One Line, One Laugh — a single sharp joke, written to entry.txt."""

import os

LINE = "I bought a standing desk to get healthier \u2014 now I sit on the floor beside it and eat crisps."

MAX_CHARS = 170


def main():
    line = LINE.strip()
    if not line:
        raise ValueError("the line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError("the line is longer than 170 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("the line must not contain a newline")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # newline="" keeps the written bytes exactly the line plus one "\n",
    # with no platform translation, so every run is byte-identical.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
