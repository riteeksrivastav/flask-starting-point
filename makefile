#!/bin/bash
.PHONY: all test
all: test

DB_NAME="flask_starting_point"
TEST_DB_NAME="test_flask_starting_point"
DB_PORT=5432
TEST_DB_PORT=5432

setup:
	virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt

install-virtualenv:
	pip install virtualenv

lint:
	find . -iname "*.py" | egrep -v "venv|pycache|.vscode" | xargs pylint

end-virtualenv:
	deactivate

test:
	ENV=TEST python -m pytest

copy-config:
	cp config/sample.env config/development.env
	cp config/sample.env config/test.env

create-db:
	createdb -h localhost -p $(DB_PORT) -U postgres $(DB_NAME)

drop-db:
	dropdb -p $(DB_PORT) --if-exists -Upostgres $(DB_NAME)

migrate:
	flask db upgrade

test-db-create:
	createdb -h localhost -p $(TEST_DB_PORT) -Upostgres $(TEST_DB_NAME)

test-db-drop:
	dropdb -p $(TEST_DB_PORT) --if-exists -Upostgres $(TEST_DB_NAME)

test-db-migrate:
	ENV=TEST flask db upgrade

rollback:
	flask db downgrade