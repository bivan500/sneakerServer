from main import app
from flask_restful import Resource
from app.main.service.user_service import get_user_by_id, set_user


@app.route("/api/sneaker/<sneaker_id>", methods=['GET'])
class UserList(Resource):
    def get(self):
        return get_user_by_id(26)
