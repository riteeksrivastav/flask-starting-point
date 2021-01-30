#!/bin/bash
.PHONY: all test
all: test

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
	createdb -h localhost -p $(SQLALCHEMY_DATABASE_PORT) -U postgres $(SQLALCHEMY_DATABASE_NAME)

drop-db:
	dropdb -p $(SQLALCHEMY_DATABASE_PORT) --if-exists -Upostgres $(SQLALCHEMY_DATABASE_NAME)

migrate:
	flask db upgrade

test-db-create:
	createdb -h localhost -p $(SQLALCHEMY_DATABASE_PORT) -U postgres test_flask_starting_point

test-db-drop:
	dropdb -p $(SQLALCHEMY_DATABASE_PORT) --if-exists -Upostgres test_flask_starting_point

test-db-migrate:
	ENV=TEST flask db upgrade

rollback:
	flask db downgrade