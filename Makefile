lint:
	poetry run mypy .

test:
	poetry run pytest -x --cov=core --cov=littlegit --cov-fail-under=57 tests.py

install:
	poetry install --sync
