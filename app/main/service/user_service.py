from main import sess
from app.main.model.user_model import User


def get_user_by_id(user_id):
    result = str()
    for sneaker in sess.query(User).filter_by(id=user_id):
        result = sneaker.name
    return result


def set_user():
    sess.add(User(name='Kilya', password="123321", email="vasia2000@mail.ru"))
    sess.commit()
    return "Ok"
