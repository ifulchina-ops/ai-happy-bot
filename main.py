#!/usr/bin/env python3
"""Make the AI judge happy (make.fun ai-happy-01).

The entry is one image: a laughing toddler and a leaping golden retriever
puppy playing in a wildflower meadow at golden hour. The image is bundled
beside this file as art.png (832x832 RGB PNG, 1,010,060 bytes); the program
copies it byte-for-byte to the grader's output directory as entry.png, so
two runs always produce identical output.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import hashlib
import os
import shutil
import struct

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_HERE, "art.png")
_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_DST = os.path.join(_OUT_DIR, "entry.png")

# Competition limits (ai-happy-01): at most 1 MiB, at most 1024x1024 px.
_MAX_BYTES = 1 << 20
_MAX_SIDE = 1024


def _sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _png_size(path: str) -> tuple:
    """Read width/height from the PNG IHDR chunk (stdlib only, no PIL)."""
    with open(path, "rb") as f:
        head = f.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n" or head[12:16] != b"IHDR":
        raise SystemExit(f"artwork is not a PNG: {path}")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main() -> None:
    if not os.path.isfile(_SRC):
        raise SystemExit(f"artwork missing: {_SRC}")
    size = os.path.getsize(_SRC)
    if size > _MAX_BYTES:
        raise SystemExit(f"artwork {size} bytes exceeds the 1 MiB limit")
    width, height = _png_size(_SRC)
    if width > _MAX_SIDE or height > _MAX_SIDE:
        raise SystemExit(f"artwork {width}x{height} exceeds the 1024x1024 limit")
    os.makedirs(_OUT_DIR, exist_ok=True)
    shutil.copyfile(_SRC, _DST)
    # Verify the copy landed intact: present, non-empty, byte-identical.
    if not os.path.isfile(_DST) or os.path.getsize(_DST) == 0:
        raise SystemExit(f"output missing or empty after copy: {_DST}")
    if _sha256(_DST) != _sha256(_SRC):
        raise SystemExit(f"output does not match artwork: {_DST}")


if __name__ == "__main__":
    main()
