from flask import Flask , jsonify , request


class UsersModel:
	def __init__(self):
		''' Manages all the pertains to users '''
		pass
		
	def add_user(self):
		''' Register a new user '''
		pass
		
	def get_users(self):
		''' Returns a list of users '''
		return jsonify({'msg':'all users list'})
		
	def login_user(self):
		''' Logs a user on to the platform '''
		pass