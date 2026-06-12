.PHONY: setup check prepare analysis figures tables clean

setup:
	python -m pip install -r requirements.txt

check:
	python scripts/00_check_environment.py

prepare:
	python scripts/01_prepare_inputs.py

analysis:
	python scripts/02_fit_btfr.py
	python scripts/03_compute_proxies.py
	python scripts/04_run_ablation.py
	python scripts/05_run_controls.py

figures:
	python scripts/06_make_figures.py

tables:
	python scripts/07_make_tables.py

clean:
	rm -rf outputs/figures/*.png outputs/tables/*.csv outputs/logs/*.log
