from flask import jsonify, request, make_response
from app import app, db
from app.models import User


@app.route('/', methods=['GET'])
def main():
    return make_response(jsonify({"message": "hello world"}), 200)

# create user


@app.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify({"message": "user created"}), 201)
    except Exception as e:
        return make_response(jsonify({"message": "error creating user"}), 500)

# get all users


@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return make_response(jsonify({'users': [user.json() for user in users]}), 200)

    except Exception as e:
        return make_response(jsonify({"message": "error getting users list"}), 500)


@app.route('/users/<int:id>', methods=['GET'])
def get_user(id: int):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({"user": user.json()}), 200)
        else:
            return make_response(jsonify({"message": 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({"message": "error getting a user"}), 500)


@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id: int):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.name = data['name']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({"message": 'user updated'}), 200)
        else:
            return make_response(jsonify({"message": 'user not found'}), 404)

    except Exception as e:
        return make_response(jsonify({"message": "error updating user"}), 500)


app.route('/users/<int:id>', methods=['DELETE'])


def delete_user(id: int):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({"message": "user deleted"}), 200)
        else:
            return make_response(jsonify({"message": 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({"message": "error updating user"}), 500)
