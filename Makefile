.PHONY: setup check prepare analysis figures tables validate paper clean

PYTHON = python3

setup:
	$(PYTHON) -m pip install --break-system-packages -r requirements.txt

check:
	$(PYTHON) scripts/00_check_environment.py

prepare:
	$(PYTHON) scripts/01_prepare_inputs.py

analysis:
	$(PYTHON) scripts/02_fit_btfr.py
	$(PYTHON) scripts/03_compute_proxies.py
	$(PYTHON) scripts/04_run_ablation.py
	$(PYTHON) scripts/05_run_controls.py

figures:
	$(PYTHON) scripts/06_make_figures.py

tables:
	$(PYTHON) scripts/07_make_tables.py

validate:
	$(PYTHON) scripts/08_validate_paper_numbers.py

paper: tables figures validate
	mkdir -p paper/tables paper/figures
	cp outputs/tables/*.csv paper/tables/
	cp outputs/figures/*.png paper/figures/

clean:
	rm -rf outputs/figures/*.png outputs/tables/*.csv outputs/logs/*.log
