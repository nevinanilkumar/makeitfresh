from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from shopproject.config import Config



db = SQLAlchemy()
bcrypt=Bcrypt()
login_manager = LoginManager()
mail = Mail()




def create_app(config_call=Config):
    app=Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "users.login"
    login_manager.message = "Please login to access the page."
    login_manager.login_message_category = "info"
    from shopproject.users.routes import users
    from shopproject.main.routes import  main
    from shopproject.shops.routes import shops
    app.register_blueprint(users)
    app.register_blueprint(shops)
    app.register_blueprint(main)
    return app


