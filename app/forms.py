from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import Required, Length, EqualTo, Email, Regexp
from models import *

class SignUpForm(Form):
	email = StringField('Email', validators=[Required(), Length(1,64), Email()])
	name = StringField('Name', validators=[Required(), Length(1,64), 
		Regexp('^[A-Za-z ]+$', 0, 'Names must have only letters and spaces.')])
	pwd1 = PasswordField('Password', validators=[Required(), Length(min=6, max=20)])
	pwd2 = PasswordField('Confirm Password', validators=[Required(), EqualTo('pwd1','Passwords must match.')])
	signup = SubmitField('Sign Up')


class LoginForm(Form):
	email = StringField('Email', validators=[Required(), Length(1,64)])
	pwd = PasswordField('Password', validators=[Required()])
	login = SubmitField('Login')