from app.user.db import Users
from app.user.exceptions import UserAlreadyExists
from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

def create(name, age):
    try:
        Users.create(name, age)
    except IntegrityError as excp:
        if isinstance(excp.orig, UniqueViolation):
            raise UserAlreadyExists
        raise excp
