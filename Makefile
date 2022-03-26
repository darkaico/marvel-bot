
start:
	python -m marvel_bot.main

test:
	poetry run pytest

lint:
	pre-commit run --all-files

docker-build:
	docker build -t marvel-bot .

docker-reset:
	docker rm marvelbot

docker-pull:
	docker pull darkaico/marvel-bot

docker-start:
	docker run --name marvelbot -d marvel-bot

clean:
	find . -iname '*.pyc' -delete
	rm -rf .pytest_cache

update-packages:
	poetry update
