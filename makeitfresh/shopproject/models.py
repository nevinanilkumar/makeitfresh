from shopproject import db,login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Seller(db.Model):
    __tablename__ = 'sellers'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    shops = db.relationship('Shop', lazy='select', backref='seller')
    
    def __str__(self):
        return f'<Seller {self.id}>'

class Buyer(db.Model):
    __tablename__ = 'buyers'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f'<Buyer {self.id}>'

class Shop(db.Model):
    __tablename__ = 'shops'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    propreiter_name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(10), unique=True, nullable=False)
    street_address = db.Column(db.String(255), nullable=False)
    district = db.Column(db.String(50), nullable=False)
    pincode = db.Column(db.String(6), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)

    def __str__(self):
        return f'<Shop {self.id}>'


    

    

    
