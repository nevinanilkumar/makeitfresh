from flask import render_template, Blueprint

main = Blueprint('main', __name__)

@main.after_request
def add_header(r):
    r.headers.add('Cache-Control', 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0')
    return r


@main.route("/")
@main.route("/home")
def home():
    return render_template("main/home.html")