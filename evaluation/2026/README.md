# 2026 YTD evaluation protocol

This directory records the controlled historical evaluation setup for the SHTENCO SEAL Sovereign Trader research line.

## Data source

Google Drive archive: `RoboForex_Top_History200001_SPLIT`.

The split archive was reconstructed and verified against the Drive checksums before use.

- part01 SHA-256: `caf428b748e24b3908ff561b5406e8c8a322cf11507af8b21b65d29da80a9071`
- part02 SHA-256: `fe1b7de4a74fa24f8349ab387a7246fdb0203d30890c650d4267800ead034000`
- part03 SHA-256: `38fc92d511b1dcf425f3b49e4c937f49db3aa13f95305b4d9d59d2586f516f45`
- reconstructed ZIP SHA-256: `7c7fa90da9fae5b346cf3d48d5466899a9d09a65149ceb0cbeaffcbaa115cf8d`

The archive contains M15/M30/H1 data for 10 FX pairs. The current LLM-trader baseline overlaps with five M15 instruments:

`EURUSD`, `GBPUSD`, `USDCHF`, `USDCAD`, `AUDUSD`.

The 2026 data available in this archive runs from 2 January 2026 through 31 July 2026. Therefore all results from this experiment must be labelled **2026 YTD**, not full-calendar-year 2026.

## Important correction to the legacy backtest

Legacy code defines the 24-hour target as `PREDICTION_HORIZON = 96` M15 bars. That is not always 24 wall-clock hours. Across the 750 candidate decisions generated from the five pairs, 151 observations span roughly 72–73 hours because of weekends.

For the controlled evaluation we retain only decisions where the +96-bar outcome is exactly +24:00 hours. This leaves **599 model decisions**.

Model-visible input is separated from future labels. A leakage audit of the generated input JSONL found zero occurrences of future price, future timestamp or actual-direction fields.

## Model target

The preferred current small Qwen checkpoint is `Qwen/Qwen3.5-4B` rather than the older Qwen2.5-3B. Qwen3.5 has no exact dense 3B checkpoint; 4B is the strongest current model in the requested ~3–4B class.

For CPU/local testing the intended quant is `Qwen3.5-4B-Q4_K_M.gguf` with a modern llama.cpp runtime.

## Control benchmark

Before Qwen inference, the deterministic fallback logic from the historical trader was evaluated on the exact-24h set. This is a control only; it is **not** a Qwen result.

- decisions: 599
- directional accuracy: 47.91%
- profit factor after entry/exit spread and 2-point round-trip slippage assumption: 0.9466
- mean net movement: -9.14 points per decision
- median net movement: -22.00 points per decision

This control establishes the minimum benchmark the Qwen-based trader should beat.

## Evaluation invariants

1. Future labels are unavailable to the model at inference time.
2. `WAIT` is a valid action and is scored through a shadow ledger rather than discarded.
3. Invalid model output becomes `NO_ACTION/repair`; it must never default to DOWN.
4. Confidence is recorded but evaluated for calibration rather than trusted as a literal probability.
5. Report gross and net results, transaction costs, abstention rate, per-symbol performance and confidence buckets.
6. Preserve each ex-ante model response before joining it with the hidden outcome file.

## Current execution status

The data pack and control benchmark are complete. The local execution environment used for this evaluation has no external DNS and currently cannot fetch the ~2.7 GB Qwen3.5-4B GGUF from Hugging Face/ModelScope. No substitute model or heuristic is being reported as Qwen. A real Qwen score should only be published after the actual checkpoint has been loaded and its responses have been generated against the sealed input set.
