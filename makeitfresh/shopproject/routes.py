from flask import Flask, render_template,url_for,redirect, request
from shopproject.forms import UserRegistrationForm
from shopproject import app


@app.route("/")
@app.route("/home")
def Home():
    return render_template("mainhome.html")

@app.route("/Register",methods=['POST','GET'])
def UserRegistration():
    form=UserRegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('Home'))
    return render_template('register/user_register.html',title="register",form=form)