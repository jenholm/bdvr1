# M69 Visual Simulation Run Instructions

From project root:

```bash
./venv/bin/python src/run_cghstc34_m69_current_governor_visual_simulation.py
python3 -m http.server 8765
```

Open:

`http://localhost:8765/runs/cghstc_34_m69_current_governor_visual_simulation/m69_visual_simulation.html`

Controls:

- Space: pause/resume
- ArrowLeft/ArrowRight: step timeline
- ArrowUp/ArrowDown: change formation run
- H: Historic initial-position mode
- N: Random initial-position mode
- R: restart
- S: save PNG snapshot

Warnings:

- DIAGNOSTIC ONLY — Diagnostic visualization only: not a validated evolutionary reconstruction.
- Product-gate governor is diagnostic/onset visualization, not the M36 mature velocity law.
- Dynamic organization score is proxy/context visualization, not Tier A direct validation.
