from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FormField
from wtforms.validators import DataRequired
from shopproject.forms import Address

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