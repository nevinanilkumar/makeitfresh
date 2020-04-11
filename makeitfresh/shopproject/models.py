from shopproject import db, login_manager
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime

# Consider changing to an alternative id for better user security.
# Not finalised.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Database model for storing user information.
# The primary key is id.
# Fields are not finalised.
class User(db.Model, UserMixin):
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


# Association table for creating many-many relationship between shops table and items table.
# Uses a compound primary key so that only unique combinations can be stored in the database.
# Two foreign keys to access information about items and shops. 
# The combinations can tell whether an item is available at a particular shop and vice versa.
shopitemlink = db.Table('shopitemlinks',
    db.Column('shop_id', db.Integer, db.ForeignKey('shops.id'), primary_key=True),
    db.Column('item_id', db.Integer, db.ForeignKey('items.id'), primary_key=True),
)


# Database model for storing shop information.
# The primary key is id.
# Uses foreign key address_id to access the shop's address.
# Address id creates one-one relationship between shop and address.
# Uses foreign key user_id to access the seller's informations and to create one-one relationship.
# Uses foreign key to get items available at the shop. 
# Use shop.items to get all the items available at a shop. 
# Not finalised.
class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    propreiter_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)
    items = db.relationship('Item', secondary = shopitemlink, backref="shops", lazy=True)
    is_authorised = db.Column(db.Boolean, default=False, nullable=False)

    def __str__(self):
        return f'<Shop {self.id}>'


# Database model for storing item information.
# The primary key is id.
# Not finalised.
class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    name = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return f'<Item {self.id}>'


# Database model for storing address information.
# Using a seperate model because a buyer might have multiple addresses. 
# This models allows users to have multiple address as user_id does not have a unique constraint.
class Address(db.Model):
    __tablename__ = "addresses"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    street_address = db.Column(db.String(255), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)

    def __str__(self):
        return f'<Address {self.id} >'


# Database models for storing order information.
# Primary key is id.
# Two foreign keys buyer_id and shop_id allows you to access buyer and seller information.
# is_delivered is a boolean field which gives true if an order is delivered.
# False if an order is pending.
# !Consider changing the default field for storing timestamps for the ordered_time column. 
# Precision is different for ordered_time and delivered_time.
# Convert time to local time before displaying on the client side.
class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    buyer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'), nullable=False)
    is_delivered = db.Column(db.Boolean, default=False, nullable=False)
    ordered_time = db.Column(db.DateTime, server_default=func.now())
    delivered_time = db.Column(db.DateTime, nullable=True)











    

    

    
