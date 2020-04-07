from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from shopproject.info import get_districts
from shopproject.models import  User
districts = get_districts()


#Basic address form to be used in all address fields. Implement better pincode checking.
class Address(FlaskForm):
    phone_number = StringField(
        label="mobile number*",
        validators=[
            DataRequired(),
            Regexp(r'^[0-9]{10}', message="Invalid Number")
        ]
    )
    street_address = StringField(
        label="street address*",
        validators=[DataRequired()],
    )
    district = SelectField(
        label="district*", 
        validators=[DataRequired()],
        choices=districts
    )
    pincode = StringField(
        label="pincode*",
        validators=[
            DataRequired(), 
            Length(6), 
            Regexp(r'^[0-9]{6}$', flags=0, message="invalid pincode")
        ],
    )

#Registration form for shopkeepers
class ShopRegistrationForm(FlaskForm):
    name = StringField(
        label="name*",
        validators=[DataRequired()],
        description= "Name of the shop"
    )
    propreiter_name = StringField(
        label="Propreiter Name*",
        validators=[DataRequired()],
        description="Name of the owner"
    )
    address = FormField(
        form_class = Address, 
        label = "Address*", 
    )
    submit=SubmitField(label="register")


#form for Login
class LoginForm(FlaskForm):
    username = StringField(
        label="username*",
        validators=[
            DataRequired(),
            Length(min=6, max=100),
            Regexp(r'^[A-Za-z0-9\._]+$', flags=0,
                   message="username can only contain alphabets, numbers and symbols . and _")
        ],
    )

    password = PasswordField(
        label="password*",
        validators=[
            DataRequired(),
            Length(min=8, max=100),
            Regexp(
                r'^(?=[a-zA-z0-9@_!%]*\d)(?=[a-zA-z0-9@_!%]*[a-zA-z])[a-zA-z0-9@_!%]{8,100}$',
                flags=0,
                message="Invalid password format. Must be atleast 8 characters long and include at least one letter and one number."
            ),
        ],
        description="Must be atleast 8 characters long and include at least one letter and one number."
    )
    submit=SubmitField(label="Login")