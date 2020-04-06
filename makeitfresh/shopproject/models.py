from shopproject import db

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    mobile_number = db.Column(db.String(10), unique=True, nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username

    
