from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from shopproject.utils import get_districts
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





