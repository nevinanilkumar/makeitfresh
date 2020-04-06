from flask import Flask, render_template,url_for,redirect, request
from shopproject.forms import UserRegistrationForm, Address, ShopRegistrationForm,LoginForm
from shopproject import app


@app.route("/")
@app.route("/home")
def Home():
    return render_template("mainhome.html")

@app.route("/register",methods=['POST','GET'])
def UserRegistration():
    form=UserRegistrationForm()
    if form.validate_on_submit():
        if form.usertype.data == "seller":
            return redirect(url_for('ShopRegistration'))
        else:
            return redirect(url_for('Home'))
    return render_template('register/user_register.html',title="User Registration",form=form)

@app.route("/register/shop", methods=["POST", "GET"])
def ShopRegistration():
    form = ShopRegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('Home'))
    return render_template("register/shop_register.html", title="Shop Registration", form=form)

#remove after testing
@app.route("/address", methods=['POST', 'GET'])
def address():
    form = Address()
    if form.validate_on_submit():
        return redirect(url_for('Home'))
    return render_template('testing/address.html', form=form)

@app.route("/login",methods=['POST', 'GET'])
def Login():
    form=LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("Home"))
    return render_template("login.html", title="login",form=form)