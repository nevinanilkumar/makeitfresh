from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError

class RegistrationShop(FlaskForm):
    # usertype=SelectField("User Type",
    # validators=[DataRequired()],
    # choices=['Consumer','Shopkeeper'])
    
    username = StringField('Username',
    validators=[DataRequired(),Length(min=2 , max=20)],
    render_kw={"placeholder": "enter username"})

    email=StringField('email',
    validators=[DataRequired(),Email()],
    render_kw={"placeholder": "enter email"})

    password= PasswordField('password',
    validators=[DataRequired()],
    render_kw={"placeholder": "enter password"})

    confirm_password= PasswordField('confirm password',
    validators=[DataRequired(),EqualTo('password')],
    render_kw={"placeholder": "confirm password"})

    shopname=StringField('Shop Name',
     validators=[DataRequired()],
     render_kw={"placeholder": "enter shop name"})

    propreitername=StringField('Propreiter name',
    validators=[DataRequired()],
    render_kw={"placeholder": "enter propreiter name"})

    mobilenumber=StringField('Mobile Number',
    validators=[DataRequired(),Length(10)],
    render_kw={"placeholder": "enter mobile number"})

    place=StringField('place',
    validators=[DataRequired()],
    render_kw={"placeholder": "enter place"} )

    submit= SubmitField('Register')

# class RegistrationCustomer(FlaskForm):
#     username = StringField('Username',
#     validators=[DataRequired(),Length(min=2 , max=20)],
#     render_kw={"placeholder": "enter username"})

#     email=StringField('email',
#     validators=[DataRequired(),Email()],
#     render_kw={"placeholder": "enter email"})

#     password= PasswordField('password',
#     validators=[DataRequired()],
#     render_kw={"placeholder": "enter password"})

#     confirm_password= PasswordField('confirm password',
#     validators=[DataRequired(),EqualTo('password')],
#     render_kw={"placeholder": "confirm password"})

#     mobilenumber=StringField('Mobile Number',
#     validators=[DataRequired(),Length(10)],
#     render_kw={"placeholder": "enter mobile number"})
    
#     submit= SubmitField('Register')