from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI '] = environ.get('DB_URL')
db = SQLAlchemy(app)


class User(db.model):
    __table__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {"id": id, "name": self.name, "email": self.email}


db.create_all()


@app.route('/', methods=['GET'])
def main():
    return make_response(jsonify({"message": "hello world"}), 200)


@app.route('/users', methods=['POST'])
def create_user():
    try:
        data= request.get_json()
        new_user= User(name=data['name'],email=data['email'])    
