# SHTENCO Synergy AGI Trader

Autonomous LLM-native trading research repository centered on **SHTENCO SEAL Sovereign Trader**: a persistent LLM trader with durable identity, top-trader philosophy, structured market beliefs, memory, internal deliberation, event-driven position management, and SEAL self-adaptation.

## Current status

This repository contains two distinct layers:

1. **Approved future architecture** — the institutional design for the new Sovereign Trader runtime.
2. **Historical research lineage** — four earlier Python generations and the four research articles that led to the design.

The historical programs under `legacy/` are preserved as research baselines. Their presence does **not** mean they are production-ready or that every technique in them remains part of the target architecture.

## Start here

- Architecture: `docs/superpowers/specs/2026-09-17-shtenco-seal-sovereign-trader-design.md`
- Repository import plan: `docs/superpowers/plans/2026-09-17-sovereign-trader-repository-import.md`
- Historical code map: `legacy/README.md`
- Research source map: `research/README.md`
- Import provenance and SHA-256 checksums: `MIGRATION_MANIFEST.json`

## Core design invariant

> The LLM is the trader. Quant models, indicators, retrieval systems, and specialist models are tools. A deterministic Capital Guardian remains outside the mutable LLM/SEAL boundary and can reject or constrain account actions.

## Historical lineage

- `legacy/v1/agi_trader_final_v1.py` — philosophy-first AGI Trader baseline.
- `legacy/v2/ai_trader_seal_rl_forward.py` — SEAL/RL/forward-testing generation.
- `legacy/v3/ai_trader_quantum_fusion_bip39_seal.py` — quantum/BIP39 fusion experiment.
- `legacy/v4/ai_trader_SEAL_with_RL_MINIMAL.py` — compact SEAL + lightweight RL generation.

## Safety and deployment status

The target system is designed for staged research, historical evaluation, shadow/paper trading, canary deployment, and only then constrained live execution. Credentials, broker secrets, model weights, adapters, local databases, generated caches, and runtime state must not be committed.
