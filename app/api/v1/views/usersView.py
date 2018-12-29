from flask import Blueprint, Flask , jsonify , request 

from app.api.v1.models.usersModel import UsersModel

userV1 = Blueprint('user_v1',__name__,url_prefix='/api/v1')

users_model = UsersModel()

@userV1.route('/users/list/', methods=['POST','GET'])
def get_sers():
	return users_model.get_users()





