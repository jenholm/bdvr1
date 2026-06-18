# M81 Response-Organization Simulation Run Instructions

From project root:

```bash
./venv/bin/python src/run_cghstc34_m81_response_organization_simulation.py
python3 -m http.server 8765
```

Open:

`http://localhost:8765/runs/cghstc_34_m81_response_organization_simulation/m81_visual_simulation.html`

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
- alpha_BTFR tracks approach to the BTFR relation; tracker values are synthetic track states.
- Coherence components are proxy/context composites, not Tier A direct validation.
