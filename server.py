from flask_restful import Api
from flask import Flask
import games_api

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = '2UHG8270YQ908GY&Y&Y7YU*&YUTG*&uwytOI&UYThUKHDAFHAfjklfjliy2r2qy983y9482'

api.add_resource(games_api.UsersListResource, '/api/users')


if __name__ == '__main__':
    app.run(debug=True)
