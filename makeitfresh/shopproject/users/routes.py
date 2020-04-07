from flask import Blueprint, render_template, redirect, url_for, request, flash
from shopproject import db, app, bcrypt
from shopproject.models import User
from shopproject.users.forms import UserRegistrationForm, LoginForm

users = Blueprint('users', __name__)


@users.route("/register",methods=['POST','GET'])
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
        return redirect(url_for('main.home'))
    return render_template("users/register.html", form=form)



@users.route("/login",methods=['POST', 'GET'])
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
#             return redirect(next_page) if next_page else redirect(url_for('main.ome'))
#         else:
#             flash(f'login unsuccessful. Check username and password ','danger')
    return render_template('users/login.html',title="Login",form=form)


