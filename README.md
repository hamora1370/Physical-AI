# Physical AI — Learning & Research OS

> A five-year, evidence-driven learning and engineering program (October 2026 → October 2031).
>
> **Working language:** Persian for planning; English for technical terms, code, and APIs.

## Mission

Develop practical competence in robotic manipulation, perception, robot learning, simulation, control, and industrial integration while maintaining focus on existing businesses. This repository records *goals, experiments, decisions, tests and evidence*—not merely completed courses.

**North-star demonstrator (2031):** a documented, safely engineered robotic manufacturing cell that receives a high-level work request, perceives parts, performs a manipulation task, recovers from defined failures, and reports execution results to an external operations system.

This is a learning repository; it is **not** a safety-certified robot controller.

## Start here

1. Read [the five-year roadmap](ROADMAP.md) and [year-one plan](docs/roadmap/Y1-2026-2027.md).
2. Read [how this system operates](docs/LEARNING_SYSTEM.md).
3. Complete [CURRENT_STATE.md](CURRENT_STATE.md); **unknown** means not yet assessed, not unskilled.
4. Open [the current 13-week plan](docs/roadmap/Q1-2026-10.md).
5. Open [NEXT_SESSION.md](NEXT_SESSION.md) at the start/end of every session.
6. Use GitHub Issues for tasks, PRs for significant updates, and tracked experiments for evidence.

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
| Current quarter | [Q1 plan](docs/roadmap/Q1-2026-10.md) |
| Skill coverage & missing prerequisites | [Skill matrix](docs/skills/SKILL_MATRIX.csv) |
| Evidence & repeatability rules | [Evidence protocol](docs/EVIDENCE_PROTOCOL.md) |
| Learning notes | [Note template](docs/templates/LEARNING_NOTE.md) |
| Experiments | [Experiment template](docs/templates/EXPERIMENT.md) |
| Review cadence | [Reviews](docs/reviews/README.md) |
| Learning resources | [Resource index](references/RESOURCES.md) |
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

**2027-01-24:** a reproducible simulated pick-and-place workflow, plus independent forward/inverse kinematics exercises and a written Q1 review. Dates are planning targets; mastery gates take precedence over the calendar.

## Privacy and licensing

This repository is currently **public**. Do not commit credentials, private customer data, unreleased business designs, sensitive recordings, identifiable factory footage, or restricted datasets. Link permitted external artifacts by immutable identifiers. Review access permissions before attaching external company systems. No license is granted by default; add one deliberately if the project becomes open source.
