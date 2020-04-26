from data import db_session
from flask_restful import reqparse, abort, Api, Resource
from flask import Flask, jsonify
from data.traning_program import Traning
from sport_func import ideal_weight, goal, set_category


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('title', required=True)
parser.add_argument('category', required=True)
parser.add_argument("duration", required=True)
parser.add_argument("program", required=True)


def abort_if_program_not_found(prog_id):
    session = db_session.create_session()
    prog = session.query(Traning).get(prog_id)
    if not prog:
        abort(404, message=f"Program {prog_id} not found")

class TraningResource(Resource):
    def get(self, prog_id):
        abort_if_program_not_found(prog_id)
        session = db_session.create_session()
        prog = session.query(Traning).get(prog_id)
        return jsonify({'traning_program': prog.to_dict(
            only=('id', 'title', 'category', "duration", "program"))})

    def delete(self, prog_id):
        abort_if_program_not_found(prog_id)
        session = db_session.create_session()
        prog = session.query(Traning).get(prog_id)
        session.delete(prog)
        session.commit()
        return jsonify({'success': 'OK'})


class TraningListResource(Resource):
    def get(self):
        session = db_session.create_session()
        prog = session.query(Traning).all()
        return jsonify({'traning_program': [item.to_dict(
            only=('id', 'title', "duration", "category", "program")) for item in prog]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        prog = Traning(
            id=args['id'],
            title=args['title'],
            program=args['program'],
            duration=args['duration'],
        category=args["category"])
        session.add(prog)
        session.commit()
        return jsonify({'success': 'OK'})