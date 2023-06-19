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
	docker-compose down -v && sudo rm -rf postgres-data

rebuild:
	docker-compose down -v && sudo rm -rf postgres-data;
	docker-compose up --build;
