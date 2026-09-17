# SHTENCO SEAL Sovereign Trader Repository Import Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Import the complete current SHTENCO AGI Trader research lineage and the approved Sovereign Trader design into `Shtenco/synergy_agi_trader` without losing provenance or modifying the legacy source files.

**Architecture:** Keep historical prototypes immutable under `legacy/`, preserve research articles under `research/articles/`, and place the approved architecture under `docs/superpowers/specs/`. Add a machine-readable migration manifest with source names, repository destinations, sizes, and SHA-256 hashes so every imported artifact is auditable. The import is documentation/archive work only; implementation of the new Sovereign Trader runtime is a separate plan built from the approved spec.

**Tech Stack:** Git/GitHub, Python 3 source archives, Markdown, JSON, SHA-256.

**Spec:** `docs/superpowers/specs/2026-09-17-shtenco-seal-sovereign-trader-design.md`

## Global Constraints

- Preserve the four legacy Python programs byte-for-byte except for repository path/name changes.
- Preserve the four research Markdown documents byte-for-byte except for repository path/name changes.
- Do not commit `__pycache__`, `.pyc`, credentials, broker secrets, model weights, or runtime state.
- Do not claim the archived Ollama `MESSAGE` workflow performs weight fine-tuning; the approved spec supersedes that interpretation.
- Keep all future mutable risk controls outside SEAL/LLM-editable code as required by the design spec.
- Every imported artifact must appear in `MIGRATION_MANIFEST.json` with a SHA-256 digest.
- Python legacy files must pass `python -m py_compile` before import is considered complete.

---

## Repository file map

- `README.md` — repository purpose, status, lineage, and navigation.
- `.gitignore` — excludes Python caches, environments, secrets, model/runtime artifacts, and local trading state.
- `MIGRATION_MANIFEST.json` — immutable import provenance and SHA-256 inventory.
- `docs/superpowers/specs/2026-09-17-shtenco-seal-sovereign-trader-design.md` — approved architecture.
- `docs/superpowers/plans/2026-09-17-sovereign-trader-repository-import.md` — this import plan.
- `legacy/README.md` — explains the four historical generations and their status.
- `legacy/v1/agi_trader_final_v1.py` — philosophy-first AGI Trader baseline.
- `legacy/v2/ai_trader_seal_rl_forward.py` — SEAL/RL/forward-test generation.
- `legacy/v3/ai_trader_quantum_fusion_bip39_seal.py` — quantum/BIP39 fusion generation.
- `legacy/v4/ai_trader_SEAL_with_RL_MINIMAL.py` — latest compact SEAL + lightweight RL generation.
- `research/README.md` — provenance and relation of source articles to the design.
- `research/articles/01_llm_trader_top_traders.md` — LLM trader with top-trader philosophy.
- `research/articles/02_continual_llm_adaptation.md` — continual LLM adaptation article.
- `research/articles/03_rl_llm_quantum_seal.md` — RL/LLM/quantum/SEAL article.
- `research/articles/04_autonomous_llm_seal_forward.md` — autonomous LLM + SEAL forward-testing article.

### Task 1: Validate source inventory

**Files:**
- Read: local source artifacts listed in `MIGRATION_MANIFEST.json`
- Test: four legacy Python files

**Interfaces:**
- Consumes: current conversation artifacts in `/mnt/data`.
- Produces: verified source inventory and digests used by Task 2.

- [ ] **Step 1: Compile every legacy Python program**

Run:
```bash
python -m py_compile \
  /mnt/data/agi_trader_final_v1.py \
  /mnt/data/ai_trader_seal_rl_forward.py \
  /mnt/data/ai_trader_quantum_fusion_bip39_seal.py \
  /mnt/data/ai_trader_SEAL_with_RL_MINIMAL.py
```
Expected: exit status `0` with no syntax errors.

- [ ] **Step 2: Compute SHA-256 and byte sizes**

Run:
```bash
sha256sum \
  /mnt/data/agi_trader_final_v1.py \
  /mnt/data/ai_trader_seal_rl_forward.py \
  /mnt/data/ai_trader_quantum_fusion_bip39_seal.py \
  /mnt/data/ai_trader_SEAL_with_RL_MINIMAL.py \
  '/mnt/data/Вставленная ​​уценка.md' \
  '/mnt/data/Вставленных ​​уценки (2).md' \
  '/mnt/data/Вставленных ​​уценки (3).md' \
  '/mnt/data/Вставленных ​​уценки (4).md' \
  /mnt/data/docs/superpowers/specs/2026-09-17-shtenco-seal-sovereign-trader-design.md
```
Expected: one 64-hex-character digest for each artifact.

- [ ] **Step 3: Confirm excluded generated files stay excluded**

Run:
```bash
find /mnt/data -type f \( -name '*.pyc' -o -path '*/__pycache__/*' \) -print
```
Expected: generated cache files may exist locally but no such path is listed in the repository import map.

### Task 2: Build repository metadata and provenance

**Files:**
- Modify: `README.md`
- Create: `.gitignore`
- Create: `MIGRATION_MANIFEST.json`
- Create: `legacy/README.md`
- Create: `research/README.md`

**Interfaces:**
- Consumes: source inventory/digests from Task 1.
- Produces: repository navigation and auditable import provenance.

- [ ] **Step 1: Write README with explicit project status**

README must state that `legacy/` is historical research code, the approved design lives in `docs/superpowers/specs/`, and no legacy program should be treated as production-ready solely because it is present in the repository.

- [ ] **Step 2: Write `.gitignore`**

It must exclude at minimum:
```gitignore
__pycache__/
*.py[cod]
.venv/
venv/
.env
.env.*
models/
checkpoints/
adapters/
runs/
logs/
*.pkl
*.joblib
*.cbm
*.gguf
*.safetensors
*.pt
*.pth
*.onnx
mt5_credentials*
broker_credentials*
```

- [ ] **Step 3: Write the migration manifest**

Each entry must contain:
```json
{
  "source_name": "agi_trader_final_v1.py",
  "destination": "legacy/v1/agi_trader_final_v1.py",
  "size_bytes": 0,
  "sha256": "64-hex-digest",
  "role": "legacy_source"
}
```
Replace `size_bytes` and `sha256` with the measured values from Task 1; do not use placeholders.

### Task 3: Import the approved design and historical corpus

**Files:**
- Create: `docs/superpowers/specs/2026-09-17-shtenco-seal-sovereign-trader-design.md`
- Create: `docs/superpowers/plans/2026-09-17-sovereign-trader-repository-import.md`
- Create: all `legacy/v*/...` files from the repository file map.
- Create: all `research/articles/...` files from the repository file map.

**Interfaces:**
- Consumes: exact bytes validated in Task 1.
- Produces: complete auditable historical corpus plus the approved future architecture.

- [ ] **Step 1: Create an isolated import branch from current `main`**

Branch name:
```text
import/seal-sovereign-trader-foundation
```

- [ ] **Step 2: Import every file according to the repository file map**

Preserve the exact UTF-8 text of source artifacts. Only repository path/name changes are permitted for the eight historical artifacts.

- [ ] **Step 3: Commit the import atomically**

Commit message:
```text
chore: import sovereign trader research foundation
```

### Task 4: Verify the GitHub import

**Files:**
- Verify: complete branch tree
- Verify: `MIGRATION_MANIFEST.json`
- Verify: four Python legacy files

**Interfaces:**
- Consumes: import branch from Task 3.
- Produces: evidence that the GitHub tree matches the local validated source set.

- [ ] **Step 1: Compare import branch with `main`**

Expected changed paths: exactly the repository file map additions/modifications; no unexpected binary/cache/credential files.

- [ ] **Step 2: Fetch imported manifest and representative source files from GitHub**

Verify the manifest is parseable JSON and the fetched source contents correspond to the imported versions.

- [ ] **Step 3: Review repository tree for forbidden artifacts**

Expected: no `__pycache__`, `.pyc`, credentials, model weights, local databases, or runtime logs.

- [ ] **Step 4: Open and merge a focused pull request**

PR title:
```text
Import SHTENCO SEAL Sovereign Trader research foundation
```

PR body must explain that the change archives the complete current research lineage and approved architecture, but does not yet implement the new runtime.

- [ ] **Step 5: Re-fetch `main` after merge**

Expected: `main` contains the complete imported tree and the merge commit is reachable as the latest repository state.
