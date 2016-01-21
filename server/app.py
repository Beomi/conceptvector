from flask import Flask, request, jsonify, session
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

api = Api(app)
bcrypt = Bcrypt(app)

from models import User

# from api import  models

# test

class CreateUser(Resource):
	def post(self):
		try:
			# Parse the arguments
			parser = reqparse.RequestParser()
			parser.add_argument('email', type=str, help='Email address to create user')
			parser.add_argument('password', type=str, help='Password to create user')

			args = parser.parse_args()

			_userEmail = args['email']
			_userPassword = args['password']

			user = User(email=_userEmail, password=_userPassword)
			db.session.add(user)
			db.session.commit()
			db.session.close()

			return {'StatusCode':'200', 'Message':'User creation success'}

		except Exception as e:
			return {'error': str(e)}

class AuthenticateUser(Resource):
	def post(self):
		try:
			# Parse the arguments
			
			parser = reqparse.RequestParser()
			parser.add_argument('email', type=str, help='Email address for Authentification')
			parser.add_argument('password', type=str, help='Password for Authentication')
			args = parser.parse_args()

			_userEmail = args['email']
			_userPassword = args['password']

			user = User.query.filter_by(email=_userEmail).first()
			if user and bcrypt.check_password_hash(user.password, _userPassword):
				session['logged_in'] = True
				status = True
			else:
				status = False
			return jsonify({'result':status})
		except Exception as e:
			return {'error':str(e)}

api.add_resource(CreateUser, '/CreateUser')
api.add_resource(AuthenticateUser, '/AuthenticateUser')

if __name__ == '__main__':
	app.run()

