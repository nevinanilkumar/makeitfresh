from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app=Flask(__name__)
app.config['SECRET_KEY']='9b11ac4263069692c46bd2a3edefba42ede6837c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.sqlite'
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='Login'
login_manager.login_message_category='info'

from shopproject import routes