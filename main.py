import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Table, Column, Integer, String, MetaData, ForeignKey
from flask import Flask, jsonify
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
app = Flask(__name__)

load_dotenv()

dbConnection = os.getenv('DB_CONNECTION')
print(dbConnection)


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    password = Column(String(45))
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

engine = create_engine("mysql+mysqldb://"+dbConnection)
conn = engine.connect()
session = sessionmaker(bind=engine)
sess = session()
Base.metadata.create_all(engine)
# metadata = MetaData()
# users_table = Table('users', metadata,
#     Column('id', Integer, primary_key=True, unique=True, nullable=False),
#     Column('name', String(45)),
#     Column('fullname', String(45)),
#     Column('password', String(45))
# )


# class Sneaker(Base):
#     def __init__(self, id, name, img, qty, price):
#         self.id = id
#         self.name = name
#         self.img = img
#         self.qty = qty
#         self.price = price
#
#     def __repr__(self):
#         return "<User('%s','%s', '%s', '%s')>" % (self.name, self.price, self.qty, self.img)


vasiaUser = User(name="vasia", password="123321", email="vasia2000@mail.ru")
sess.add(vasiaUser)
sess.commit()

@app.route("/api/sneaker/<post_id>", methods=['GET'])
def sneaker_id(post_id):
    result = conn.execute(text("SELECT * FROM sneaker WHERE id=" + post_id))
    return jsonify([dict(r) for r in result])


@app.route("/api/sneaker/", methods=['GET'])
def get_sneakers():
    result = conn.execute(text("SELECT * FROM sneaker"))
    return jsonify([dict(r) for r in result])


@app.route("/api/register/", methods=['POST'])
def register():
    result = conn.execute(text("SELECT * FROM sneaker"))
    return jsonify([dict(r) for r in result])


if __name__ == '__main__':
    app.run(debug=True)