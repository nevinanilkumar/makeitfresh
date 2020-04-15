from flask import Blueprint, render_template, redirect, url_for, request, flash, Response, abort, session
from flask_login import login_user, current_user, logout_user, login_required
from is_safe_url import is_safe_url
from shopproject import db, bcrypt
from shopproject.models import User
from shopproject.users.forms import UserRegistrationForm, LoginForm, ResetPasswordForm, RequestResetForm
from shopproject.users.utils import send_email

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
            user.authenticated = True
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
    user = User.query.get(current_user.id)
    user.authenticated=False
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account")
@login_required
def account():
    return render_template("users/account.html", title="Account")

#Not complete
@users.route("/reset_password", methods=["GET", "POST"])
def request_reset_password():
    form = RequestResetForm()
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    else:
        if form.validate_on_submit() and request.method == "POST":
            user = User.query.filter_by(email=form.email.data).first()
            if user:
                recipient_email = user.email
                token = user.get_reset_token()

                url = url_for("users.reset_password_token", token = token, _external=True)
                email_body = """
                To reset your password,
                please click the following link
                {}
                """.format(url)
                send_email(recipient_email, email_body)
                flash(f"Please check your inbox for steps to reset your password." ,"info")
                return redirect(url_for("main.home"))
            else:
                flash(f"User does not exist.", "failure")
    return render_template("users/test_request_reset.html", form=form)

#Not complete
@users.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password_token(token):
    form = ResetPasswordForm()
    if current_user.is_authenticated:
        return redirect(url_for("main.home"))
    user = User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token", "danger")
        return redirect(url_for("users.request_reset_password"))
    else:
        if form.validate_on_submit() and request.method == "POST":
            user.password = bcrypt.generate_password_hash(form.new_password.data).decode("utf-8")
            db.session.commit()
            flash(f"Password has been reset successfully. You may now login.", "success")
            return redirect(url_for("users.login"))

    return render_template("users/test_reset_password.html", form=form, token=token)






