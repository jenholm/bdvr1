# M82 Response-Organization Landscape Simulation Run Instructions

From project root:

```bash
./venv/bin/python src/run_cghstc34_m82_organization_landscape_simulation.py
python3 -m http.server 8765
```

Open:

`http://localhost:8765/runs/cghstc_34_m82_organization_landscape_simulation/m82_visual_simulation.html`

Controls:

- Space: pause/resume
- ArrowLeft/ArrowRight: step timeline
- ArrowUp/ArrowDown: change formation run
- H: Historic initial-position mode
- N: Random initial-position mode
- R: restart
- S: save PNG snapshot

Warnings:

- DIAGNOSTIC ONLY — Response-organization visualization: not a validated evolutionary reconstruction.
- A_gov = min(A_star, A_gas, A_sigma, A_HI) is a phenomenological governor model.
- Gate components are illustrative, not validated direct dynamical measurements.
