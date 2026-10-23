# Instructions for AI collaborators and assistants

This repository is an evidence-based five-year Physical AI learning program, **not** an autonomous production robot controller.

## Start by reading
1. `README.md`, `ROADMAP.md`
2. `CURRENT_STATE.md`, `NEXT_SESSION.md`
3. `docs/roadmap/Q1-2026-10.md` (or the currently active quarter)
4. `docs/skills/SKILL_MATRIX.csv` and `docs/EVIDENCE_PROTOCOL.md`
5. Active GitHub Issues, tests and experiment reports

## Before proposing work
- Identify the current quarter's exit gate and the relevant skill IDs.
- Check existing Issues and linked evidence; never duplicate active work without justification.
- Keep WIP <= 2; do not expand all five years into detailed tasks.
- Prefer one small, verifiable improvement and show exactly how to check it.
- Do not silently upgrade ROS/Gazebo or change the technology stack: propose an ADR.

## After implementing
- Run the most relevant tests; say explicitly if execution could not be verified.
- Update links/evidence only for performed work.
- Never claim ROS, a physical robot, datasets, trained policies or industrial readiness exist without verification.
- Update `NEXT_SESSION.md` with one next step; update skill matrix only with proof.
- Put reusable knowledge in Markdown in this repository rather than relying on chat memory.

## Safety and privacy
- Repository is PUBLIC. Never commit secrets, customer materials, sensitive video, unreleased designs or ERP infrastructure details.
- Generated motion policies must not bypass hardware safety interlocks or the independent safety layer.
- Avoid unsupervised physical actuation or safety-critical deployments.
- Avoid rewriting Git history, overriding files unexpectedly or deleting evidence.

## Review format
Use `docs/reviews/AI_REVIEW_PROMPT.md` for weekly/quarterly audit. Separate **verified findings**, **uncertainties** and **recommended next actions**.
