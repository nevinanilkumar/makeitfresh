from flask import Blueprint, render_template, redirect, url_for, request, flash, Response, abort
from flask_login import login_user, current_user, logout_user, login_required
from is_safe_url import is_safe_url
from shopproject import db, bcrypt
from shopproject.models import User
from shopproject.users.forms import UserRegistrationForm, LoginForm

users = Blueprint('users', __name__)

@users.after_request
def add_header(r):
    r.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return r


@users.route("/register",methods=['POST','GET'])
def userRegistration():
    form=UserRegistrationForm()
    if current_user.is_authenticated:
            return redirect(url_for('main.home'))
    elif request.method=="POST" and form.validate_on_submit():
        hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(
            user_type=form.user_type.data,
            username=form.username.data.strip(),
            email=form.email.data.strip(),
            first_name=form.first_name.data.strip(),
            last_name=form.last_name.data.strip(),
            password=hashed_password,
        )
        db.session.add(new_user)
        db.session.commit()
        flash(f"Your account has been created. Please login to view the website.", 'success')
        return redirect(url_for('users.login'))
    elif request.method == "POST" and (not form.validate_on_submit()):
        flash(f'Please correct the incorrect fields.')
    return render_template("users/register.html", title="Register", form=form)


@users.route("/login",methods=['POST', 'GET'])
def login():
    form=LoginForm()
    if current_user.is_authenticated:
            return redirect(url_for('main.home'))
    elif form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page= request.args.get('next')
            if next_page and not is_safe_url(next_page, allowed_hosts={"127.0.0.1:5000"}):
                return abort(400)
            flash(f'Login successful. Welcome {user.username}!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        
        else:
            flash(f'Login unsuccessful. Check username and password ','danger')
    return render_template('users/login.html',title="Login",form=form)


@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account")
@login_required
def account():
    return render_template("users/account.html", title="Account")



