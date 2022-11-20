
start:
	poetry python -m marvel_bot.main

test:
	poetry run pytest

lint:
	pre-commit run --all-files

clean: ## Remove generated files.
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

update-packages:
	poetry update
