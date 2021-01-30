import pytest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.user.db import Users
from sqlalchemy import delete
from psycopg2.errors import UniqueViolation

app = Flask(__name__)
app.config.from_object('config.AppConfig')
db = SQLAlchemy(app)

def clear_db():
    table = Users.__table__
    stmt = delete(table)
    db.session.execute(stmt)
    db.session.commit()
    db.session.close()

def test_should_create_user_if_does_not_exist():
    clear_db()
    Users.create('Bob', 23)
    data = Users.query.filter_by(name='Bob').first()
    assert data.name == 'Bob'
    assert data.age == 23
    clear_db()
    
def test_should_raise_unique_violation_if_user_with_same_name_already_registered():
    clear_db()
    Users.create('Bob', 23)
    try:
        Users.create('Bob', 21)
    except Exception as excp:
        assert isinstance(excp.orig, UniqueViolation) == True
    finally:
        clear_db()
    