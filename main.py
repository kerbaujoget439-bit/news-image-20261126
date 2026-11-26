#!/usr/bin/env python3
"""Hand over the finished front page for Thursday 26 November 2026.

The picture itself (entry.png, stored beside this file) is the entry:
a single-page newspaper summary of that one day's world news -- 39
story units, a UTC timeline, a pinned world map and a written date
check. It was drawn while the entry was being built; at grading time
this program only carries a copy of the picture into the output
folder, byte for byte, so two runs always produce identical bytes.

Nothing is downloaded and nothing is rendered here: the program uses
only the Python standard library, and it refuses to write anything
that is not a valid PNG identical to the picture in the repository.
"""

import hashlib
import os
import shutil
import sys

PICTURE = "entry.png"

# The first eight bytes of every PNG file.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def picture_path() -> str:
    """Where the picture lives: next to this program."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, PICTURE)


def output_path() -> str:
    """Where the grader wants the picture: $MAKEFUN_OUTPUT_DIR or /output."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, PICTURE)


def sha256(path: str) -> str:
    """Hash a file in small chunks so big pictures stay cheap."""
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def is_png(path: str) -> bool:
    """Check the file really starts with the PNG signature."""
    with open(path, "rb") as handle:
        return handle.read(len(PNG_MAGIC)) == PNG_MAGIC


def run() -> int:
    source = picture_path()
    target = output_path()
    if not is_png(source):
        print(f"error: {source} is not a PNG file", file=sys.stderr)
        return 1
    if os.path.getsize(source) > 1048576:
        print(f"error: {source} is over the 1 MiB cap", file=sys.stderr)
        return 1
    shutil.copyfile(source, target)
    if sha256(source) != sha256(target):
        print("error: the copy does not match the original", file=sys.stderr)
        return 1
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
