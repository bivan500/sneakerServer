from flask import jsonify, request
from common.db import db_session
from common.models import User
from flask_restful import Resource
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
# @app.route("/api/sneaker/<sneaker_id>", methods=['GET'])
# def get_sneaker(sneaker_id):
#     session = sessionmaker(bind=engine)
#     sess = session()
#     result = str()
#     for sneaker in db_session.query(Sneaker).filter_by(id=sneaker_id):
#         result = sneaker.name
#     return result
#
#
# @app.route("/api/sneaker/", methods=['GET'])
# def get_sneakers():
#     session = sessionmaker(bind=engine)
#     sess = session()
#     sneaker_list = list()
#     for instance in sess.query(Sneaker).order_by(Sneaker.id):
#         sneaker_list.append(instance.name)
#     return jsonify(sneaker_list)


class User_resources(Resource):
    def post(self):
        exist_user = User.query.filter(User.email == request.form['email']).first()
        # exist_user = db_session.query_property(User).filer(User.email == request.form['email']).first()
        if not exist_user:
            if len(str(request.form['password'])) > 5:
                if request.form['password'] == request.form['second_password']:
                    set_user = User(
                        name=request.form['name'],
                        password=bcrypt.generate_password_hash(request.form['password']).decode('utf-8'),
                        email=request.form['email'])
                    db_session.add(set_user)
                    db_session.commit()
                    return jsonify(request.form)
                else:
                    response_object = {
                        'Error': 'Password must equal in two rows'
                    }
                    return response_object, 409
            else:
                response_object = {
                    'Error': 'Password cannot be lower than 6 words',
                }
                return response_object, 409
        else:
            response_object = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return response_object, 409
