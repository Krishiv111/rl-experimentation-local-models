# rl-experimentation-local-models

Small-scale, honest experiments in post-training: can a self-built, verifiable
reward signal (tests pass / tests fail) actually improve a small open model,
measured on held-out tasks?

## The idea

Reward is 1 if a task's tests pass, 0 if they don't. Tasks come from
deliberately re-breaking correct code with realistic bug patterns (off-by-one,
wrong comparator, bad boundary, missing base case) instead of hand-writing an
unlimited task bank.

## Status

- [x] Stage 0 — first 5 tasks + PASS/FAIL runner (`tasks.py`, `runner.py`)
- [ ] Stage 1 — baseline: score a few existing models on the task set
- [ ] Stage 2 — scale to ~150 tasks via automated bug injection, held-out split
- [ ] Stage 3 — SFT a small open model on passing samples
- [ ] Stage 4 — GRPO (reward = tests passing) on the same model
- [ ] Stage 5 — held-out before/after table + write-up

## Files

- `tasks.py` — the broken functions (the environment)
- `runner.py` — the grader (PASS/FAIL per task, this is the reward signal)
