from common.db import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    password = Column(String(255), unique=True)
    email = Column(String(45))


class Sneaker(Base):
    __tablename__ = 'sneaker'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    img = Column(String(255))
    qty = Column(Integer)
    price = Column(Integer)

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.name, self.price, self.qty, self.img)