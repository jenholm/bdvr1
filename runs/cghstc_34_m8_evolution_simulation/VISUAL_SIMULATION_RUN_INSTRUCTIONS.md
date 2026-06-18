# M8 visual simulation run instructions

The visual simulation is a browser-based p5.js sketch generated from the current M8 SPARC-lite diagnostic artifacts.

## Regenerate the simulation artifacts

From the project root:

```bash
cd /home/jenholm/photonland/cghs/cghstc_34
./venv/bin/python src/run_cghstc34_m8_evolution_simulation.py
```

## Run it in a browser

Because browsers often block local JavaScript/data access from `file://` URLs, serve the project root:

```bash
cd /home/jenholm/photonland/cghs/cghstc_34
python3 -m http.server 8765
```

Then open:

http://localhost:8765/runs/cghstc_34_m8_evolution_simulation/m8_visual_simulation.html

## Controls

- Space: pause/resume
- Left/Right: step backward/forward along the selected galaxy evolution track
- Up/Down: switch among the UGC07125 seed reference and the 50 randomized baby-galaxy formations
- R: restart the selected track
- S: save a PNG snapshot from the browser

## What you are seeing

- Left panel: SPARC-lite quality-1 galaxies in maturity-feature space (`f_star` vs `log10 Sigma_b`), colored by implied activation.
- Right panel: animated juvenile-to-mature disk cartoon. It starts from UGC07125, then automatically loops through 50 deterministic epsilon-randomized gas-rich baby-galaxy formations before returning to UGC07125.
- Bottom panel: time history of `A_gov` for the selected track.

Claim boundary: this is a visual diagnostic only, not an accepted BDVR model term and not a proof of the juvenile-to-mature mechanism.
