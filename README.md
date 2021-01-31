# Flask Starting Point
This is a simple microservice based CRUD application in Flask. It will be a guide to project structure for flask applications.
It supports 
* Logging.
* Config management for different envs.

## Dependencies
* Python 3.7
* Postgresql 10

## How to
### Build 
1. To install virtualevn run `pip install virtualenv`
2. Run `make setup` to start virtualenv and install all the dependencies
3. Run `make copy-config` to setup the config.
4. Create database locally by running `make create-db`
5. Migrate all table schemas by running `make migrate`. 
6. To stop the virtualenv run `deactivate`

### Run test
1. Create test database by running `make test-db-create`
2. Migrate all table schemas by running `make test-db-migrate`. 
3. To run tests run `make test`

### Run
1. To start the server locally run `make run-server`

## Directory Structure
├── README.md
├── app
│   ├── __init__.py
│   ├── handler
│   │   ├── ping.py
│   │   ├── response.py
│   │   └── user.py
│   └── user
│       ├── db.py
│       ├── exceptions.py
│       └── service.py
├── config
│   ├── __init__.py
│   ├── development.env
│   ├── sample.env
│   └── test.env
├── makefile
├── migrations
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── daaf9d29dafc_initial_migration.py
├── requirements.txt
├── test
│   ├── handler
│   │   ├── test_ping.py
│   │   └── test_user.py
│   └── user
│       ├── test_db.py
│       └── test_service.py
└── wsgi.py

## TODO
* Support monitoring