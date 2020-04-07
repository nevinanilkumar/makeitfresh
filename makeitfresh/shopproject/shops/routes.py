from flask import Blueprint, redirect, render_template, url_for
from shopproject.shops.forms import ShopRegistrationForm
from shopproject.models import Shop
from shopproject import db, bcrypt

shops = Blueprint('shops', __name__)
#gets redirected from userregistration form
@shops.route("/shop/register", methods=["POST", "GET"])
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
        return redirect(url_for('main.home'))
    return render_template("shops/register.html", title="Shop Registration", form=form)
