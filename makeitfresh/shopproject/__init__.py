from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from shopproject.config import Config



db = SQLAlchemy()
bcrypt=Bcrypt()
# from .models import User

# login_manager = LoginManager(app)
# login_manager.login_view='Login'
# login_manager.login_message_category='info'

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))



def create_app(config_call=Config):
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    from shopproject.users.routes import users
    from shopproject.main.routes import  main
    from shopproject.shops.routes import shops
    app.register_blueprint(users)
    app.register_blueprint(shops)
    app.register_blueprint(main)
    return app

