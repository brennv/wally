install:
	python3 -m venv .; \
	source bin/activate; \
	pip install --upgrade pip
	pip install -r requirements.txt; \

run:
	source bin/activate; \
	python3 run.py; \

test:
	source bin/activate; \
	py.test -q tests.py; \

freeze:
	source bin/activate; \
	pip freeze > requirements.txt; \
