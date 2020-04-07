from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, FormField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp
from shopproject.models import  User
from shopproject.forms import Address

#Registration form common for all users.
class UserRegistrationForm(FlaskForm):
    user_type = SelectField(
        label="usertype*",
        validators=[DataRequired()],
        description="Do you want to register as a buyer or a seller?",
        choices=[('buyer', 'Buyer'), ('seller', 'Seller')],
    )
    username = StringField(
        label="username*",
        validators=[
            DataRequired(),
            Length(min=6, max=100),
            Regexp(r'^[A-Za-z0-9\._]+$', flags=0,
                   message="username can only contain alphabets, numbers and symbols . and _")
        ],
    )
    email = StringField(
        label="email*",
        validators=[DataRequired(), Email()],
    )
    first_name = StringField(
        label="first name*",
        validators=[DataRequired()],
    )
    last_name = StringField(
        label="last name*",
        validators=[DataRequired()],
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
    confirm_password = PasswordField(
        label="confirm password*",
        validators=[
            DataRequired(),
            EqualTo('password', message="Passwords do not match.")
        ],
        description="Please re-enter your password"
    )
    submit = SubmitField(label="register")

    def validate_username(self, username):
        """To check if the username entered by the user is unique. 
        If it is not unique, the function will raise a validation error."""
        
        user_exists = User.query.filter_by(username=username.data.strip()).first()
        if user_exists:
            raise ValidationError("Username exists. Please enter a unique username.")
    
    def validate_email(self, email):
        """To check if the email entered by the user is unique.
        If it is not unique, the function will raise a validation error."""

        email_exists = User.query.filter_by(email=email.data.strip()).first()
        if email_exists:
            raise ValidationError("Email is associated with another account. Please enter a different email address.")




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