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

up-dbg:
	docker-compose -f docker-compose.debug.yml up

up-dbg-build:
	docker-compose -f docker-compose.debug.yml up --build