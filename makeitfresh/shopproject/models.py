from shopproject import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_type = db.Column(db.String(10), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f'<User {self.id}>'
    

class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    propreiter_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    street_address = db.Column(db.String(255), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    authorised = db.Column(db.Boolean, default=False, nullable=False)

    def __str__(self):
        return f'<Shop {self.id}>'


    

    

    
