#!/usr/bin/env python3
"""news-image-20261125 entry, MERGED (Python 3.13, standard library only).

The image is the entry.png beside this file, drawn by generate.py in this
repo from the verified news of Wednesday 25 November 2026 (see MERGE.md).
This program only copies it to /output/entry.png — the copy pattern the
bounty rules explicitly allow ("the simplest program copies an image
already in the repo").

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output,
or pass --output <dir>:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    args = sys.argv[1:]
    if "--output" in args:
        out_dir = args[args.index("--output") + 1]
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png is missing next to main.py")
    if os.path.getsize(SRC) == 0:
        raise SystemExit("entry.png is empty")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(out_dir, "entry.png"))
    print("wrote", os.path.join(out_dir, "entry.png"),
          os.path.getsize(os.path.join(out_dir, "entry.png")), "bytes")


if __name__ == "__main__":
    main()
