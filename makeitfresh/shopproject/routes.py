from flask import Flask, render_template,url_for,redirect, request
from shopproject.forms import UserRegistrationForm,LoginForm
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

@app.route("/buyerhome")
def BuyerHome():
    return render_template("buyerhome.html")

@app.route("/shopkeeperhome")
def ShopKeeperHome():
    return render_template("shopkeeperhome.html")

@app.route("/login",methods=['POST','GET'])
def Login():
    form=LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('Home'))
    return render_template("login.html",title="Login",form=form)