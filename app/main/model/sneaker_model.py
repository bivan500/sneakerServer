from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class Sneaker(Base):
    __tablename__ = 'sneaker'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    img = Column(String(255))
    qty = Column(Integer)
    price = Column(Integer)

    def __repr__(self):
        return "<User('%s','%s', '%s', '%s')>" % (self.name, self.price, self.qty, self.img)