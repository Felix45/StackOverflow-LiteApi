from flask import Flask
from app.api.v1.views.usersView import userV1

	
def create_app():
	app = Flask(__name__)
	app.register_blueprint(userV1,url_prefix='/api/v1')

	@app.route('/')
	def index():
		return 'hello, world Felix'
			
	return app
	