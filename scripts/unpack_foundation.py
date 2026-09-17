#!/usr/bin/env python3
"""Reconstruct, verify, and extract the archived Sovereign Trader foundation."""

from __future__ import annotations

import base64
import hashlib
import io
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS_DIR = ROOT / "archive" / "foundation_xz"
EXPECTED_SHA256 = "6d32722a9eefc174b38b33fbad9df4df9a41cd63393f1ecc027e992a428e44b0"


def main() -> None:
    parts = sorted(PARTS_DIR.glob("part-*"))
    if len(parts) != 15:
        raise SystemExit(f"Expected 15 archive parts, found {len(parts)}")

    encoded = b"".join(part.read_bytes().strip() for part in parts)
    payload = base64.b64decode(encoded, validate=True)
    digest = hashlib.sha256(payload).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"Archive SHA-256 mismatch: {digest}")

    with tarfile.open(fileobj=io.BytesIO(payload), mode="r:xz") as tf:
        root = ROOT.resolve()
        for member in tf.getmembers():
            target = (ROOT / member.name).resolve()
            if root != target and root not in target.parents:
                raise SystemExit(f"Unsafe archive path: {member.name}")
        tf.extractall(ROOT, filter="data")

    print(f"Foundation extracted successfully; archive SHA-256={digest}")


if __name__ == "__main__":
    main()
