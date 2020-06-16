build:
	docker build -t marvel-bot .

reset:
	docker rm marvelbot

start:
	docker run --name marvelbot -d marvel-bot

test:
	docker exec marvelbot python -m pytest