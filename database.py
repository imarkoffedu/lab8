# Відповідає за підключення до бази даних 
# та створення сесії для взаємодії з нею

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Base

engine = create_engine('sqlite:///orders_orm.db', echo=False)

def create_session():
    Base.metadata.create_all(engine)
    return Session(engine)


def close_session(session):
    session.close()