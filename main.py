"""News-image entry: copy the finished day-summary picture to the output slot.

The picture itself (entry.png, drawn at build time from the verified
27 November 2026 stories) sits next to this file. This program does one
thing: it reads those exact bytes and writes them to the directory the
grader names, so both grading runs produce the identical file.
Only the Python standard library is used; there is no network access.
"""

import hashlib
import os
import pathlib
import shutil
import sys


def _picture_path():
    """Return the path of the bundled picture next to this program."""
    here = pathlib.Path(__file__).resolve().parent
    return here / "entry.png"


def _target_dir():
    """Return the writable output directory for this run.

    The grader sets MAKEFUN_OUTPUT_DIR; a plain OUTPUT_DIR is accepted as
    a fallback for local runs. An empty value counts as unset, so the
    default /output is used instead of failing on a blank path.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        chosen = os.environ.get(name)
        if chosen and chosen.strip():
            return pathlib.Path(chosen)
    return pathlib.Path("/output")


def _fingerprint(path):
    """Return the sha256 hex digest of a file's bytes."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    source = _picture_path()
    if not source.is_file():
        print("missing bundled picture: %s" % source, file=sys.stderr)
        return 1
    wanted = _fingerprint(source)
    destination_dir = _target_dir()
    destination_dir.mkdir(parents=True, exist_ok=True)
    destination = destination_dir / "entry.png"
    shutil.copyfile(source, destination)
    got = _fingerprint(destination)
    if got != wanted:
        print("copy mismatch: %s != %s" % (got, wanted), file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)" % (destination, destination.stat().st_size, got))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
