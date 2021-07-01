import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from flask import Flask, jsonify


app = Flask(__name__)

load_dotenv()

dbConnection = os.getenv('DB_CONNECTION')
print(dbConnection)


engine = create_engine("mysql+mysqldb://"+dbConnection)
conn = engine.connect()


@app.route("/api/sneaker/<post_id>", methods=['GET'])
def sneaker_id(post_id):
    result = conn.execute(text("SELECT * FROM sneaker WHERE id=" + post_id))
    return jsonify([dict(r) for r in result])


@app.route("/api/sneaker/", methods=['GET'])
def get_sneakers():
    result = conn.execute(text("SELECT * FROM sneaker"))
    return jsonify([dict(r) for r in result])


if __name__ == '__main__':
    app.run(debug=True)