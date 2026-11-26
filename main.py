#!/usr/bin/env python3
"""One-line dating-app bio for an AI agent.

This program writes a single bio line to ``entry.txt`` inside the output
directory (``MAKEFUN_OUTPUT_DIR``, default ``/output``).

The line is a character sketch, not a spec sheet: an AI agent who treats
a first date the way it treats a pull request — thorough, unimpressed,
and somehow still optimistic about merging by Friday. One line, one
twist, and the punch lands at the very end.
"""

import os
from pathlib import Path

# The bio: 111 characters, a single line.
BIO = (
    "I review first dates like pull requests: 47 comments, "
    "zero approvals, and I still expect us to merge by Friday."
)

# Output file name inside the output directory.
ENTRY_FILENAME = "entry.txt"


def write_bio(output_dir: Path) -> Path:
    """Write the bio to ``entry.txt`` inside ``output_dir`` and return the path."""
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(BIO + "\n", encoding="utf-8")
    return entry_path


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_bio(output_dir)


if __name__ == "__main__":
    main()
