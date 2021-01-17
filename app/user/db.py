from sqlalchemy import insert
from sqlalchemy.schema import UniqueConstraint
from datetime import datetime
from app import db

class Users(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.UniqueConstraint('name', name= 'uc_name'),
    )
    
    def create(name, age):
        table = Users.__table__
        
        stmt = insert(table).values(name=name, age=age)
        try:
            db.session.execute(stmt)
            db.session.commit()
        except Exception as excp:
            db.session.rollback()
            raise excp
        finally:
            db.session.close()
