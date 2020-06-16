build:
	docker build -t marvel-bot .

delete_container:
	docker rm marvelbot

start:
	docker run --name marvelbot -d marvel-bot

test:
	docker exec marvelbot python -m pytest