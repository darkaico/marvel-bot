[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=darkaico_marvel-bot&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=darkaico_marvel-bot)

# Marvel Bot

Simple bot that fetch data from [Marvel API](https://developer.marvel.com/docs#!/public)
and broadcaste information into Twitter and a Telegram channel

## Twitter Profile

See it in action and follow [here](https://twitter.com/marvelibot) !

## Telegram Channel

Join in this [link](https://t.me/marveldata)

## Libraries

- [Tweepy](https://www.tweepy.org/): For Twitter posts and interactions
- [Requests](https://requests.readthedocs.io/en/master/): for Marvel API fetch and Telegram calls.
- [Dacite](https://github.com/konradhalas/dacite): for API responses to dataclasses objects
- [Schedule](https://schedule.readthedocs.io/en/stable/) for scheduling jobs at certain time.
- [Python dotenv](https://github.com/theskumar/python-dotenv): simplifies env var uses.
- [Pytest](https://docs.pytest.org/en/latest/): just it, test it.

## Extras

I added Sentry to the project for monitorizing more info [here](https://docs.sentry.io/platforms/python/)

## Thanks

Based on the idea from @fermezz [Star Wars bot](https://github.com/fermezz/starwars-bot)
