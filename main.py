import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text, Table, Column, Integer, String, MetaData, ForeignKey
from flask import Flask, jsonify, request
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
Base.metadata.create_all(engine)


@app.route("/api/sneaker/<sneaker_id>", methods=['GET'])
def get_sneaker(sneaker_id):
    session = sessionmaker(bind=engine)
    sess = session()
    result = str()
    for sneaker in sess.query(Sneaker).filter_by(id=sneaker_id):
        result = sneaker.name
    return result


@app.route("/api/sneaker/", methods=['GET'])
def get_sneakers():
    session = sessionmaker(bind=engine)
    sess = session()
    sneaker_list = list()
    for instance in sess.query(Sneaker).order_by(Sneaker.id):
        sneaker_list.append(instance.name)
    return jsonify(sneaker_list)


@app.route("/api/register/<name>", methods=['GET'])
def register(name):
    session = sessionmaker(bind=engine)
    sess = session()
    set_user = User(name=name, password="123321", email="vasia2000@mail.ru")
    sess.add(set_user)
    sess.commit()
    return "q"


@app.route("/api/test", methods=['POST'])
def post_test():
    session = sessionmaker(bind=engine)
    sess = session()
    set_user = User(name=request.form['name'], password=request.form['password'], email=request.form['email'])
    sess.add(set_user)
    sess.commit()
    return jsonify(request.form)


if __name__ == '__main__':
    app.run(debug=True)