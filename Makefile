# see. https://ricardoanderegg.com/posts/makefile-python-project-tricks/
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules


build:
	docker-compose build;

up:
	docker-compose up;

up-build:
	docker-compose up --build;

up-build-d:
	docker-compose up -d --build;

down-v:
	docker-compose down -v --remove-orphans && sudo rm -rf postgres-data

rebuild:
	docker-compose down -v --remove-orphans && sudo rm -rf postgres-data;
	docker-compose up --build;

rebuild-d:
	docker-compose down -v --remove-orphans && sudo rm -rf postgres-data;
	docker-compose up --build -d;

d-test:
	# Rebuilds container and runs docker test
	docker-compose build web-test && docker-compose run web-test pytest tests -x -o log_cli=true
