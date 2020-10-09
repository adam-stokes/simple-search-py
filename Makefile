SEARCHTERM ?= life

build:
	docker build . -t simple-search

check:
	docker run simple-search pytest -v test/test_matches.py

run:
	docker run -e SEARCHTERM=$(SEARCHTERM) simple-search python3 eg/main.py


.phony: check run build
all: check
