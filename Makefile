.PHONY: all

SHELL=/bin/bash -c

format_all:
	poetry run ruff format .
	poetry run ruff check --fix .

typecheck_all:
	poetry run mypy .

format_changed:
	poetry run ruff format $(shell git diff --name-only | grep .py) $(shell git ls-files -o --exclude-standard | grep .py)
	poetry run ruff check --fix $(shell git diff --name-only | grep .py) $(shell git ls-files -o --exclude-standard | grep .py)

typecheck_changed:
	poetry run mypy $(shell git diff --name-only | grep .py) $(shell git ls-files -o --exclude-standard | grep .py)

i18n_init:
	poetry run pybabel extract -o translations/messages.pot .
	poetry run pybabel init -i translations/messages.pot -d translations -l ru
	poetry run pybabel init -i translations/messages.pot -d translations -l en

i18n_update:
	poetry run pybabel extract -o translations/messages.pot .
	poetry run pybabel update -i translations/messages.pot -d translations
	
i18n_compile:
	poetry run pybabel compile -d translations