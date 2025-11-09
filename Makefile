VENV=.venv

init:
	python3 -m venv $(VENV) || true
	$(VENV)/bin/pip install -r requirements.txt

run: init
	. $(VENV)/bin/activate; python clean.py --in_csv data/sample.csv --out_csv data/out.csv --col text

test: init
	. $(VENV)/bin/activate; PYTHONPATH=. pytest -q
