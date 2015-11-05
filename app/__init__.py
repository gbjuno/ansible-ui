from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from flask.ext.mail import Mail

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
login_manager = LoginManager()
mail = Mail()

def create_app():
	global manager, bootstrap, db, moment, login_manager

	app = Flask(__name__)
	
	from web import main as main_blueprint
	#from auth import auth as auth_blueprint
	app.register_blueprint(main_blueprint)

	app.config['SECRET_KEY'] = 'gf37888676'
	app.config['DEBUG'] = True
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ansible:ansible@172.17.0.25/ansible'
	app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

	bootstrap.init_app(app)
	db.init_app(app)
	moment.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	return app