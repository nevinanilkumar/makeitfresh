from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='9b11ac4263069692c46bd2a3edefba42ede6837c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.sqlite'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
# from .models import User

# login_manager = LoginManager(app)
# login_manager.login_view='Login'
# login_manager.login_message_category='info'

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

from shopproject import routes