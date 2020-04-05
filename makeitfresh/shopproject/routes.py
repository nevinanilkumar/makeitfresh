from flask import Flask, render_template,url_for,redirect
from shopproject.forms import RegistrationShop
from shopproject import app


@app.route("/")
@app.route("/home")
def Home():
    return render_template("mainhome.html")

@app.route("/Register",methods=['POST','GET'])
def ShopRegistration():
    form=RegistrationShop()
    #if form.validate_on_submit:
       # return redirect(url_for('Home'))
    #else:
    return render_template('ShopRegister.html',title="register",form=form)