
start:
	python -m app.main

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov

lint:
	pre-commit run --all-files

docker-build:
	docker build -t marvel-bot .

docker-reset:
	docker rm marvelbot

docker-start:
	docker run --name marvelbot -d marvel-bot

clean:
	find . -iname '*.pyc' -delete
	rm -rf .pytest_cache

export:
	git archive master | gzip > latest.tgz
