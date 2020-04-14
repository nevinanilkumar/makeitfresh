import pytest
from shopproject import create_app, db
from shopproject.config import Test
from shopproject.models import User
from sqlalchemy.exc import OperationalError
from flask import url_for
from flask_login import current_user
current_user = None
@pytest.fixture
def app():
    app=create_app()
    app.config.from_object(Test)
    with app.app_context():
        try:
            user = User.query.filter_by(id=1).first()
        except OperationalError:
            db.create_all()
            db.session.commit()
        yield app
    
def test_app(app):
    client = app.test_client()
    resp = client.get("/")
    assert app.config["TESTING"]
    assert not app.config["WTF_CSRF_ENABLED"]
    assert resp.status_code == 302

def register_user(app,**kwargs):
    client = app.test_client()
    resp = client.post("/register",
    data = {
        "user_type":kwargs.get("user_type"),
        "username":kwargs.get("username"),
        "email":kwargs.get("email"),
        "first_name":"Test",
        "last_name":"User",
        "password":kwargs.get("password"),
        "confirm_password":kwargs.get("confirm_password"),
        "submit":"register",
    },
    follow_redirects = kwargs.get("redirect"))
    return resp

def login_user(app, **kwargs):
    client=app.test_client()
    resp = client.post("/login",
        data = {
            "username":kwargs.get("username"),
            "password":kwargs.get("password"),
            "remember":"False",
            "submit":"login",
        },
    follow_redirects=kwargs.get("redirect"))
    return resp

def test_validate_register(app):
    resp = register_user(app, 
        user_type="buyer", 
        username="testuser1", 
        email="testuser1@company.com",
        password="testing123",
        confirm_password="testing123",
        redirect=False
    )
    assert resp.status_code == 302
    assert not User.query.get(1).is_authenticated()

def test_login_success(app):
    resp = login_user(app,username="testuser1", password="testing123", redirect=False)
    global current_user
    assert resp.status_code == 302
    assert User.query.get(1).is_authenticated()

def test_clear_database(app):
    with app.app_context():
        db.drop_all()
        db.session.commit()



