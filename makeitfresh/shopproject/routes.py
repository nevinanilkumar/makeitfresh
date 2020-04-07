from flask import Flask, render_template,url_for,redirect, request, flash
from shopproject.forms import  Address, ShopRegistrationForm,LoginForm
from .register_forms import UserRegistrationForm
from shopproject.models import User, Shop
from shopproject import app,db,bcrypt
# from flask_login import login_user,current_user,logout_user,login_required

# @login_required
@app.route("/")
@app.route("/home")
def home():
    return render_template("mainhome.html")

@app.route("/register",methods=['POST','GET'])
def userRegistration():
    form=UserRegistrationForm()
    if request.method=="POST" and form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data)
        new_user = User(
            user_type=form.user_type.data,
            username=form.username.data.strip(),
            email=form.email.data.strip(),
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            password=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Your account has been successfully created.", 'success')
        return redirect(url_for('home'))
    return render_template("register/user_register.html", form=form)



#gets redirected from userregistration form
@app.route("/register/shop", methods=["POST", "GET"])
def shopRegistration():
    form = ShopRegistrationForm()
    if form.validate_on_submit():
        new_shop=Shop(
            name=form.name.data,
            propreiter_name=form.propreiter_name.data,
            phone_number=form.phone_number.data,
            street_address=form.address.street_address.data,
            district=form.address.district.data,
            pincode=form.address.pincode.data,
            authorised=False,
        )
        db.session.add(new_shop)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("register/shop_register.html", title="Shop Registration", form=form)

#remove after testing
@app.route("/address", methods=['POST', 'GET'])
def address():
    form = Address()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('testing/address.html', form=form)

# def whichuser(user1,user2):
#     if user1:
#         return user1
#     return user2

@app.route("/login",methods=['POST', 'GET'])
def login():
    form=LoginForm()
#     if form.validate_on_submit():
#         user1= Buyer.query.filter_by(username=form.username.data).first()
#         user2= Seller.query.filter_by(username=form.username.data).first()
#         user = whichuser(user1,user2)
#         if user and bcrypt.check_password_hash(user.password,form.password.data):
#             login_user(user)
#             next_page=request.args.get('next')
#             flash(f'login successful for {form.username.data}!','success')
#             return redirect(next_page) if next_page else redirect(url_for('Home'))
#         else:
#             flash(f'login unsuccessful. Check username and password ','danger')
    return render_template('login.html',title="Login",form=form)




