#!/usr/bin/env python3
"""The Worst Pizza Topping — make.fun entry.

Writes one funny line pitching a terrible pizza topping to
/output/entry.txt. The topping: terms and conditions — forty pages
of fine print on a pizza, zero flavor, and you still have to scroll
to the bottom before your first bite. The line is 159 characters,
inside the gate's 1–200 character window, and the program re-checks
that window before writing.
"""

import os
import sys

LINE = (
    "Try our new pizza topped with terms and conditions \u2014 forty pages "
    "of fine print, zero flavor, and you still have to scroll to the "
    "bottom before your first bite."
)

MIN_LEN = 1
MAX_LEN = 200


def validate(line: str) -> bool:
    """The gate: UTF-8 text, 1-200 chars, not only whitespace, one line."""
    if not (MIN_LEN <= len(line) <= MAX_LEN):
        return False
    if not line.strip():
        return False
    if "\n" in line or "\r" in line:
        return False
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    line = LINE.strip()
    if not validate(line):
        print("invalid entry line", file=sys.stderr)
        return 1

    data = line.encode("utf-8")
    tmp = path + ".tmp"
    with open(tmp, "wb") as f:
        f.write(data)
    os.replace(tmp, path)

    with open(path, "rb") as f:
        if f.read() != data:
            print("verify failed", file=sys.stderr)
            return 1
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
