from flask import render_template, Blueprint, request, json, redirect, url_for
from flask_login import login_required, current_user
from shopproject.models import Shop
from sqlalchemy import or_
main = Blueprint('main', __name__)

@main.after_request
def add_header(r):
    r.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return r


@main.route("/")
@main.route("/home")
@login_required
def home():
    if current_user.email_verified:
        if current_user.user_type == "buyer":
            search_entry = request.args.get("shop")
            if request.args.get("shop"):
                shops = []
                for shop in Shop.query.filter(or_(
                    Shop.name.startswith(search_entry.lower()),
                    Shop.name.startswith(search_entry.upper()),
                    Shop.name.startswith(search_entry)
                    )).all():
                    shops.append({
                        "name":shop.name.lower(),
                        "phone_number":shop.phone_number,
                    })
                return json.jsonify(shops)
        return render_template("main/buyer.html")
    else:
        return render_template("users/test_email_verif_hint.html")
    return render_template("main/home.html")

@main.route("/buyerhome")
def BuyerHome():
    return render_template("homebuyer.html")