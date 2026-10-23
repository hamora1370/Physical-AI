# How to operate the Learning & Research OS

## Sources of truth

- Goals/scope: `ROADMAP.md`.
- Quarterly objectives: `docs/roadmap/`.
- Personal baseline: `CURRENT_STATE.md`.
- Coverage and demonstrated skills: `docs/skills/SKILL_MATRIX.csv`.
- Task execution: GitHub Issues (one issue per tangible outcome, linked to code/evidence).
- Resume point: `NEXT_SESSION.md`.
- Experiments: `experiments/` metadata; large assets outside Git with versioned references.
- Strategic choices: Architecture Decision Records under `docs/decisions/`.

Do not create parallel copies of the same task status in chat and GitHub. Chat assists; GitHub is canonical.

## Workflow for a new topic

1. Confirm the topic belongs to the current quarterly exit gate.
2. Check prerequisites in the skill matrix.
3. Create a learning Issue with a measurable Definition of Done.
4. Study source → explain concept from memory → implement → test unfamiliar examples.
5. Commit notes/code/results with references and dates.
6. Update skill level only if linked evidence demonstrates it.
7. Close the Issue and update `NEXT_SESSION.md`.

## Workflow for an experiment

1. Declare hypothesis, baseline, independent variables and success metric **before** running.
2. Record code SHA, environment, robot/firmware/calibration, model/dataset/policy version and seed when relevant.
3. Record successes **and** failures; distinguish training from held-out evaluation.
4. Create a report with reproducible commands and immutable artifact references.
5. Decide keep/revise/stop; link experiment to an Issue and skill evidence.

## Limits and drift control

- WIP = 2 (at most one theory and one implementation task active).
- New tools/papers land in an Issue/backlog; do not interrupt sprint without blocker/security reason.
- Cap management overhead near 10% of study time.
- Deep-plan only the current quarter. Years 2–5 are hypotheses to revise quarterly.
- Before accepting a new work item: which exit gate does it serve? what will be demonstrated?

## Mastery levels

L0 unknown/not started; L1 explain without reference; L2 independently implement and test;
L3 diagnose and generalize to unfamiliar controlled conditions; L4 integrate, measure, and defend a realistic engineering design.

Levels are topic-specific, not a self-rating of intelligence. Missing evidence means **unverified**, not failure.

## Review cadence

- After each session (5 min): update NEXT_SESSION and push code/logs.
- Weekly (15–20 min): review blockers and plan next two tasks.
- Monthly (45 min): closed-book retrieval and regression tests.
- Quarterly (up to 2 h): audit skill coverage and exit gates; replan next quarter.
- Annually: evaluate portfolio, budget, time capacity, and commercial direction.

Use [review templates](reviews/README.md) rather than creating free-form, hard-to-compare reports.
