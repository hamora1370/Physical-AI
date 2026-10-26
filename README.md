# Physical AI — Learning & Research OS

> A five-year, evidence-driven learning and engineering program (October 2026 → October 2031).
>
> **Working language:** Persian mentoring/reviews; English repository docs, code, identifiers, and technical terms.

## Mission

Develop practical competence in robotic manipulation, perception, robot learning, simulation, control, and industrial integration while maintaining focus on existing businesses. This repository records *goals, experiments, decisions, tests and evidence*—not merely completed courses.

**North-star demonstrator (2031):** a documented, safely engineered robotic manufacturing cell that receives a high-level work request, perceives parts, performs a manipulation task, recovers from defined failures, and reports execution results to an external operations system.

This is a learning repository; it is **not** a safety-certified robot controller.

## Start here

1. Read [the five-year roadmap](ROADMAP.md) and [year-one plan](docs/roadmap/Y1-2026-2027.md).
2. Read [how this system operates](docs/LEARNING_SYSTEM.md).
3. Complete [CURRENT_STATE.md](CURRENT_STATE.md); **unknown** means not yet assessed, not unskilled.
4. Open [the current 13-week SCARA-01 project plan](docs/roadmap/Q1-2026-10.md), [SCARA-01 engineering concept](docs/projects/SCARA-01-CONCEPT.md), and [robot-learning requirements](docs/projects/SCARA-01-LEARNING-PLATFORM.md).
5. Open [NEXT_SESSION.md](NEXT_SESSION.md) at the start/end of every session.
6. Follow [the Q1 milestone (#5)](https://github.com/hamora1370/Physical-AI/issues/5); start from [Issue #1](https://github.com/hamora1370/Physical-AI/issues/1). Use Issues for tasks, PRs for significant updates, and tracked experiments for evidence.

## Operating rules

- **One active theory issue + one active implementation issue max** (WIP limit = 2).
- Only plan the current quarter in detail; review distant years quarterly.
- Every skill claim requires reproducible evidence (test, explanation, benchmark, or demonstrator).
- Record what failed, not just what succeeded.
- Revisit the roadmap quarterly; park new ideas in the backlog rather than changing focus mid-sprint.
- Start at **5 focused hours/week** in the first two years; increase only if other business responsibilities allow it.
- Keep safety interlocks and hardware protection separate from any AI policy or high-level planner.

## Navigation

| Area | Source of truth |
| --- | --- |
| Long-range direction | [ROADMAP.md](ROADMAP.md) |
| WSL2 on-demand setup | [PhysicalAI installation and safe switching](docs/infrastructure/WSL2-ON-DEMAND.md) |
| Current quarter | [Q1 SCARA-01 plan](docs/roadmap/Q1-2026-10.md) | 
| Anchor robot engineering project | [SCARA-01 concept and design gates](docs/projects/SCARA-01-CONCEPT.md) |
| Future robot-learning readiness | [Command, state, gripper feedback, data contract](docs/projects/SCARA-01-LEARNING-PLATFORM.md) · [ADR-0002](docs/decisions/ADR-0002-scara-learning-platform.md) |
| Skill coverage & missing prerequisites | [Skill matrix](docs/skills/SKILL_MATRIX.csv) |
| Evidence & repeatability rules | [Evidence protocol](docs/EVIDENCE_PROTOCOL.md) |
| Learning notes | [Note template](docs/templates/LEARNING_NOTE.md) |
| Experiments | [Experiment template](docs/templates/EXPERIMENT.md) |
| Review cadence | [Reviews](docs/reviews/README.md) |
| Learning resources | [Resource index](references/RESOURCES.md) |
| AI review / collaboration | [Review prompt](docs/reviews/AI_REVIEW_PROMPT.md) · [AGENTS.md](AGENTS.md) |
| Last state, next action | [NEXT_SESSION.md](NEXT_SESSION.md) |
| Scope decisions | [ADR-0001](docs/decisions/ADR-0001-scope.md) |

## Repository structure

```text
docs/
  roadmap/       annual / quarterly goals
  skills/        coverage and mastery levels
  decisions/     architecture / strategy decisions
  reviews/       weekly / monthly / quarterly reviews
  templates/     reusable learning and experiment notes
experiments/     reproducible runs, not raw private datasets
exercises/       minimal code exercises
tests/           automated checks
references/      curated resources
.github/         issue and PR templates, CI
```

## First checkpoint

**2027-01-24:** SCARA-01 engineering requirements and design including learning-ready measured-state/episode interface choices, independently verified FK/IK, a reproducible **simulated R-R-P pick-and-place** workflow (or a recorded simulation blocker with reproducible fallback) and a Q1 review. Physical 2R prototyping is an optional stretch; safe staged four-axis/gripper physical integration can continue in Q2. Dates remain planning targets; mastery gates take precedence.

## Privacy and licensing

This repository is currently **public**. Do not commit credentials, private customer data, unreleased business designs, sensitive recordings, identifiable factory footage, or restricted datasets. Link permitted external artifacts by immutable identifiers. Review access permissions before attaching external company systems. No license is granted by default; add one deliberately if the project becomes open source.
