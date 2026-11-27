#!/usr/bin/env python3
"""The Friday Wire — Friday 27 November 2026 in one image.

Pure-stdlib renderer: it only copies the pre-drawn broadsheet image
(entry.png, shipped next to this file) to the requested output path.
No drawing, no network, no third-party imports.
"""

import hashlib
import os
import sys
from pathlib import Path


def _source_image():
    """Locate the bundled broadsheet image next to this script."""
    here = Path(__file__).resolve().parent
    candidate = here / "entry.png"
    if candidate.is_file():
        return candidate
    fallback = Path.cwd() / "entry.png"
    if fallback.is_file():
        return fallback
    raise FileNotFoundError("entry.png not found next to main.py")


def _output_path():
    """Resolve where the image must be written."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return Path(out_dir) / "entry.png"
    return Path("/output/entry.png")


def _copy_image_bytes(src, dst):
    """Copy src to dst in chunks and return the sha256 of what was written.

    Chunked reads keep memory flat even if the bundled PNG grows; the
    digest is computed from the exact bytes written, so a later compare
    of source and output hashes proves the copy is byte-identical.
    """
    digest = hashlib.sha256()
    dst.parent.mkdir(parents=True, exist_ok=True)
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
            fout.write(chunk)
    return digest.hexdigest()


def main():
    src = _source_image()
    dst = _output_path()
    checksum = _copy_image_bytes(src, dst)
    # Deterministic, byte-identical re-runs: same input bytes, same output.
    print(f"wrote {dst} sha256={checksum}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
