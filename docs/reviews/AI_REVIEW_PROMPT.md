# Physical AI Review — reusable instructions

Use this prompt when reviewing the repository with an AI assistant connected to GitHub.

> Review the current state of the `Physical-AI` repository as an evidence-based five-year robotics learning program. First fetch and read `ROADMAP.md`, `CURRENT_STATE.md`, `NEXT_SESSION.md`, the active quarterly roadmap, `docs/skills/SKILL_MATRIX.csv`, active Issues and recent commits/experiment reports. Do not assume completed work from chat history. Distinguish verified artifacts, claimed but unverified work, and blocked/unstarted tasks. Compare outcomes with the current quarterly exit gate. Identify missing prerequisites, topics neglected, recurring technical failures, overdue reviews, and scope drift. Recommend at most two immediately actionable Issues (one theory, one implementation), with measurable Definition of Done and time budgets. State whether the program is harming core business priorities if evidence exists; otherwise say it is unknown. Do not mark skills completed without evidence. Update files or create Issues only when authorized for those actions.

## Weekly report sections
1. Snapshot: active gate, linked commit, Issues, actual study time if documented.
2. Evidence: passing tests, reproducible demos, experiments and missing proof.
3. Gaps: missing prerequisites, regressions, retention and unresolved blockers.
4. Drift check: new tools/frameworks vs quarterly objective.
5. Next 1–2 Issues with explicit acceptance criteria.
6. One resume action for NEXT_SESSION.md.

## Quarterly additions
- Coverage audit of all planned skill IDs and linked evidence.
- Gate decision: advance, extend or replan, with reasons.
- Updated risk/budget/time assumptions.
- Proposed ADRs for major toolchain or strategy changes.

## Anti-hallucination rules
No inferred test pass, equipment purchase, model accuracy or ROS installation; no optimistic percentage based on files created. If a check is unavailable, label it **not verified**.
