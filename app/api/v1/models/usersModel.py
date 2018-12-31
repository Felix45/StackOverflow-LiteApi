from flask import Flask , jsonify , request
from app.api.v1.helpers.usersHelper import UsersHelper
from werkzeug.security import generate_password_hash,check_password_hash

users  = []
helper = UsersHelper()




class UsersModel:
	
	def __init__(self):
		''' Manages all that pertains to users '''
		pass
		
	def add_user(self,user_request):
		''' Register a new user '''
		global users , helper
		new_user = {}
		keys_expected = ['username','email','password','cpassword']
		
		validator = helper.is_valid_user_request(keys_expected,request)
		
		print validator
		
		if not validator[0]:
			return validator[1] , 400
		
		validator = helper.is_blank_field(request)
		
		if not validator[0]:
			return validator[1] , 400
			
		user_id   = len(users)+1
		username  = user_request.get_json()['username']
		email     = user_request.get_json()['email']
		password  = user_request.get_json()['password']
		cpassword = user_request.get_json()['cpassword']
		
		validator = helper.is_available(username,'username',users)
		
		if not validator[0]:
			return validator[1] , 400
			
		validator = helper.is_available(email,'email',users)
		
		if not validator[0]:
			return validator[1] , 400
		
		validator = helper.is_valid_email(email)
			
		if not validator[0]:
			return validator[1] , 400
			
		validator = helper.is_valid_password(password,cpassword)
		
		if not validator[0]:
			return validator[1] , 400
			
		
		new_user['user_id']   = user_id
		new_user['username']  = username
		new_user['email']     = email
		new_user['password']  = generate_password_hash(password)
	
		
		users.append(new_user)
		
		return jsonify({'msg':'user: {} was added successfully'.format(username)})
		
		
		
		
		
		
	def get_users(self):
		''' Returns a list of users '''
		global users
		
		if(len(users) == 0 ):
			return jsonify({'msg':'No user was found'})
		
		return jsonify(users) 
		
	def login_user(self):
		''' Logs a user on to the platform '''
		pass