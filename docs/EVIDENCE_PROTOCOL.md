# Evidence protocol and benchmarking

**Principle:** confidence comes from repeatable evidence, not course completion or demo videos.

## For a learning claim

Record: concept, closed-book explanation, implementation commit SHA, tests, at least one unfamiliar test, current limitations, assessed level L0–L4. Update skills CSV `evidence_ref` with a permalink/relative file path.

## For each robot experiment

- immutable experiment ID (e.g. `EXP-2027-003`), date, task, hypothesis;
- environment (OS/ROS versions, machine, simulator) and source commit;
- hardware/firmware/control parameters or simulation model version;
- model/policy/dataset versions and seeds when applicable;
- clearly named baseline, conditions, randomization and sample count;
- successes, failures, failure categories, timings, interventions and safety stops;
- held-out evaluation different from training demonstrations;
- reproducible command/script and artifact reference; key conclusions.

## Common metrics

**Task success**: successful completions / eligible attempts with defined pass/fail.
**Cycle time**: distribution, not only mean.
**Intervention rate**: human interventions per attempt/hour.
**Recovery**: eligible failures recovered / recovery opportunities.
**Safety events**: independently logged; zero observed events does not prove formal safety.

Publish task definitions before measuring. Record denominator, exclusions and aborts. Do not convert a successful short video into a generalization claim.

## Data policy

Large datasets, videos, model weights and private images live in access-controlled storage with immutable IDs/checksums. Git stores metadata/links, not raw private data. Never upload customer-specific identifiers or private credentials.
