from flask import Flask, render_template,url_for,redirect, request
from shopproject.forms import UserRegistrationForm, Address, ShopRegistrationForm,LoginForm
from shopproject.models import Seller,Buyer,Shop
from shopproject import app,db,bcrypt
from flask_login import login_user,current_user,logout_user,login_required


@app.route("/")
@app.route("/home")
def Home():
    return render_template("mainhome.html")

@app.route("/register",methods=['POST','GET'])
def UserRegistration():
    form=UserRegistrationForm()
    if form.validate_on_submit():
        #hashing
        hashed_password=bcrypt.generate_password_hash(form.password.data)
        if form.usertype.data == "seller":
            user=Seller(username=form.username.data,password=hashed_password,first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('ShopRegistration'))
        else:
            user=Buyer(username=form.username.data,password=hashed_password,first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('Home'))
    return render_template('register/user_register.html',title="User Registration",form=form)

#gets redirected from userregistration form
@app.route("/register/shop", methods=["POST", "GET"])
def ShopRegistration():
    form = ShopRegistrationForm()
    if form.validate_on_submit():
        shop=Shop(name=form.name.data,propreiter_name=form.propreiter_name.data,phone_number=form.phone_number.data,
        street_address=form.street_address.data,district=form.district.data,pincode=form.pincode.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('Home'))
    return render_template("register/shop_register.html", title="Shop Registration", form=form)

#remove after testing
@app.route("/address", methods=['POST', 'GET'])
def address():
    form = Address()
    if form.validate_on_submit():
        

        return redirect(url_for('Home'))
    return render_template('testing/address.html', form=form)

def whichuser(user1,user2):
    if user1:
        return user1
    else:
        return user2

@app.route("/login",methods=['POST', 'GET'])
def Login():
    form=LoginForm()
    if form.validate_on_submit():
        user1= Buyer.query.filter_by(username=form.username.data).first() 
        user2= Seller.query.filter_by(username=form.username.data).first()
        user = whichuser(user1,user2)
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            next_page=request.args.get('next')
            flash(f'login successful for {form.username.data}!','success')
            return redirect(next_page) if next_page else redirect(url_for('Home'))
        else: 
            flash(f'login unsuccessful.check username and password ','danger')    
    return render_template('login.html',title="Login",form=form)

        


