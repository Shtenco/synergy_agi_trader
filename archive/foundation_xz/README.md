# Sovereign Trader foundation archive

This directory contains the complete base64-encoded `tar.xz` foundation bundle split into ordered Git-friendly parts.

Archive SHA-256 after concatenating, base64-decoding, and writing the binary `tar.xz`:

```text
6d32722a9eefc174b38b33fbad9df4df9a41cd63393f1ecc027e992a428e44b0
```

The archive contains the complete repository target tree prepared on 2026-09-17: the approved Sovereign Trader design, repository import plan, four immutable legacy Python generations, four research articles, repository READMEs, `.gitignore`, and `MIGRATION_MANIFEST.json`.

Run `python scripts/unpack_foundation.py` from the repository root to reconstruct and validate the archive and extract its tree into the working copy. The script refuses to continue if the archive SHA-256 does not match.
