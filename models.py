# Визначення моделей даних для бази даних

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Goods(Base):
    __tablename__ = 'goods'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

class Clients(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Orders(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    goods_id = Column(Integer, ForeignKey('goods.id'))
    quantity = Column(Integer)

    client = relationship("Clients")
    goods = relationship("Goods")