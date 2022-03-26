
start:
	python -m marvel_bot.main

test:
	poetry run pytest

lint:
	pre-commit run --all-files

clean:
	find . -iname '*.pyc' -delete
	rm -rf .pytest_cache

update-packages:
	poetry update
