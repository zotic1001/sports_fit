from data import db_session
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify
from data.users import User
from sport_func import ideal_weight, goal, set_category


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('name', required=True)
parser.add_argument('email', required=True)
parser.add_argument("age", required=True)
parser.add_argument("height", required=True)
parser.add_argument("weight", required=True)
parser.add_argument("gender", required=True)
parser.add_argument("need", required=True)


def abort_if_user_not_found(user_id):
    session = db_session.create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")

class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('id', 'name', 'email', "age", "height", "weight", "gender"))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('id', 'name', "email", "age", "height", "weight", "gender")) for item in user]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = User(
            id=args['id'],
            name=args['name'],
            email=args['email'],
            age=args['age'],
            height = args['height'],
            weight=args['weight'],
            gender=args['gender'],
        need=args["need"])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})

