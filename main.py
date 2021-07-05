from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_restful import Api
from resources.sneaker import User_resources
from common.db import db_session

app = Flask(__name__)

api = Api(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


api.add_resource(User_resources, '/registration')


if __name__ == '__main__':
    app.run(debug=True)