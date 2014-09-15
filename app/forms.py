from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, FieldList, FormField, TextAreaField
from wtforms.validators import *
from wtforms_html5 import IntegerField, DecimalField

class SignUpForm(Form):
	email = StringField('Email', validators=[InputRequired(), Length(1,64), Email()])
	name = StringField('Name', validators=[InputRequired(), Length(1,64), 
		Regexp('^[A-Za-z ]+$', 0, 'Names must have only letters and spaces.')])
	pwd1 = PasswordField('Password', validators=[InputRequired(), Length(6,20)])
	pwd2 = PasswordField('Confirm Password', validators=[InputRequired(), EqualTo('pwd1','Passwords must match.')])
	signup = SubmitField('Sign Up')


class LoginForm(Form):
	email = StringField('Email', validators=[InputRequired(), Length(1,64)])
	pwd = PasswordField('Password', validators=[InputRequired()])
	login = SubmitField('Login')

class ReferenceForm(Form):
	book = StringField('Book')
	page = StringField('Page', validators=[Regexp('^[A-Za-z0-9]+$', 0, 'Letters and numbers only.')])

class WeaponDamageForm(Form):
	dmg_type = StringField('Damage Type', 
		validators=[Regexp('^[A-Za-z ]+$', 0, 'Lowercase letters only.')])
	amount = StringField('Amount')

class AttributeModForm(Form):
	attribute = StringField('Attribute', validators=[Regexp('^[A-Za-z ]+$', 0, 'Lowercase letters only.')])
	modifier = IntegerField('Modifier')

class AddItemForm(Form):
	#required features
	name = StringField('Item Name', validators=[InputRequired()])
	references = FieldList(FormField(ReferenceForm), 'References', min_entries=1, validators=[InputRequired()])
	weight = DecimalField('Weight', validators=[InputRequired(), NumberRange(min=0)], places=2)
	value = DecimalField('Value', validators=[InputRequired(), NumberRange(min=0)], places=2)
	item_type = StringField('Item Type', validators=[InputRequired(), Regexp('^[A-Za-z ]+$', 0, 'Lowercase letters only.')])
	
	#weapon features
	weapon_types = FieldList(StringField('Weapon Type', 
		validators=[Optional(), Regexp('^[A-Za-z ]+$', 0, 'Lowercase letters only.')]))
	#damage = FieldList(FormField(WeaponDamageForm), 'Damage', validators=[Optional()])
	
	critical = StringField('Critical', validators=[Optional()])
	range_increment = IntegerField('Range', validators=[Optional(), NumberRange(min=0)]) #in ft
	
	#armor features
	armor_type = StringField('Armor Type', validators=[Optional(), Regexp('^[A-Za-z ]+$', 0, 'Lowercase letters only.')])
	armor_bonus = IntegerField('Armor Bonus', validators=[Optional(), NumberRange(min=0)])
	max_dex_bonus = IntegerField('Max Dex Bonus', validators=[Optional(), NumberRange(min=0)])
	armor_check_penalty = IntegerField('Armor Check Penalty', validators=[Optional(), NumberRange(max=0)]) #negative numbers
	arcane_spell_failure = IntegerField('Arcane Spell Failure', validators=[Optional(), NumberRange(min=0, max=100)]) #in %
	movement_speed = IntegerField('Movement Speed', validators=[Optional(), NumberRange(min=0)])
	
	#miscellaneous features
	total_uses = IntegerField('Total Uses', validators=[Optional(), NumberRange(min=0)])
	#attribute_modifiers = FieldList(FormField(AttributeModForm), 'Attribute Modifiers', validators=[Optional()])
	#relevant_spells = FieldList(StringField('Relevant Spell', validators=[Regexp('^[A-Za-z ]+$', 0, 'Lowercase letters only.')]), validators=[Optional()])
	description = TextAreaField('Description', validators=[Optional()])
	submit = SubmitField('Submit')



		