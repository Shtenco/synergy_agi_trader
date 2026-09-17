# Legacy research lineage

This directory preserves the four historical SHTENCO AGI Trader generations exactly as imported. They are archival research baselines for migration into the new `SHTENCO SEAL Sovereign Trader` architecture.

## v1 — `agi_trader_final_v1.py`

Philosophy-first AGI Trader generation. It introduced the central idea that the LLM should be a discretionary trader with explicit Soros/Jones/Dalio/Livermore principles, HOLD/CASH, stop/target reasoning, and freedom to reject a trade.

## v2 — `ai_trader_seal_rl_forward.py`

SEAL/RL/forward-test generation. It explored self-adaptation, forward testing, replay-like learning, and an autonomous LLM trading loop.

## v3 — `ai_trader_quantum_fusion_bip39_seal.py`

Experimental fusion generation combining CatBoost, quantum-derived features, BIP39-derived features, SEAL concepts, and LLM reasoning. Quantum/BIP39 components are preserved for research provenance; they are not automatically part of the new production path.

## v4 — `ai_trader_SEAL_with_RL_MINIMAL.py`

Compact SEAL + lightweight RL generation. It contains the `USE/SKIP/REDUCE` meta-policy idea that is retained conceptually as MetaIntuition in the Sovereign Trader design.

## Migration rule

Do not patch these files in place when implementing the new architecture. New production code should live outside `legacy/`; legacy files remain stable reference artifacts whose original import hashes are recorded in `MIGRATION_MANIFEST.json`.
