test:
	poetry run pytest

lint: ## Lint all files.
	pre-commit run --all-files

docker-build:
	docker build -t marvel-bot .

docker-reset:
	docker rm marvelbot

docker-start:
	docker run --name marvelbot -d marvel-bot

export:
	git archive master | gzip > latest.tgz
