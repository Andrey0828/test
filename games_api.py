import sqlite3

from flask_restful import Resource
from flask import jsonify
from parser_games import parser
import config


class UsersListResource(Resource):
    def post(self):
        args = parser.parse_args()
        email = args['email']
        config.conf = email
        return jsonify({'success': 'OK'})

    def get(self):
        return jsonify({'config': config.conf})
