from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FieldList, FormField, TextAreaField, SelectField
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

#class ReferenceForm(Form):
#	book = StringField('Book', validators=[InputRequired()])
#	page = StringField('Page', validators=[InputRequired(), Regexp('^[A-Za-z0-9]+$', 0, 'Letters and numbers only.')])

class WeaponTypesForm(Form):
	unarmed = BooleanField('unarmed', validators=[Optional()])
	light = BooleanField('light', validators=[Optional()])
	melee = BooleanField('melee', validators=[Optional()])
	one_handed = BooleanField('one-handed', validators=[Optional()])
	two_handed = BooleanField('two-handed', validators=[Optional()])
	ranged = BooleanField('ranged', validators=[Optional()])
	simple = BooleanField('simple', validators=[Optional()])
	martial = BooleanField('martial', validators=[Optional()])
	exotic = BooleanField('exotic', validators=[Optional()])

class WeaponDamageForm(Form):
	dmg_type = StringField('Type', 
		validators=[Optional(), Regexp('^[a-z ]+$', 0, 'Lowercase letters and spaces only.')])
	amount = StringField('Amount')

class AttributeModForm(Form):
	attribute = StringField('Attribute', validators=[Regexp('^[a-z ]+$', 0, 'Lowercase letters and spaces only.')])
	modifier = IntegerField('Modifier')

class AddItemForm(Form):
	#required features
	name = StringField('Item Name', validators=[InputRequired()])
	weight = DecimalField('Weight', validators=[NumberRange(min=0)], places=2)
	value = DecimalField('Value', validators=[NumberRange(min=0)], places=2)
	reference = StringField('Reference', validators=[InputRequired()])
#	references = FieldList(FormField(ReferenceForm), 'References', min_entries=1, validators=[InputRequired()])
	
	#weapon features
	weapon_types = FormField(WeaponTypesForm, 'Weapon Types')
	damage = FieldList(FormField(WeaponDamageForm), 'Damage', min_entries=1, validators=[Optional()])
	
	critical = StringField('Critical', validators=[Optional()])
	range_increment = IntegerField('Range Increment', validators=[Optional(), NumberRange(min=0)]) #in ft
	
	#armor features
	armor_type = SelectField('Armor Type', validators=[Optional()], 
		choices=[("", "none"),
				 ("light", "light"),
				 ("medium", "medium"),
				 ("heavy", "heavy"),
				 ("shield", "shield"),
				 ("miscellaneous", "miscellaneous")])
	body_slot = SelectField('Body Slot', validators=[Optional()], 
		choices=[("", "none"),
				 ("body", "body"),
				 ("head", "head"),
				 ("face", "face"),
				 ("throat", "throat"),
				 ("shoulders", "shoulders"),
				 ("arms", "arms"),
				 ("hands", "hands"),
				 ("ring", "ring"),
				 ("torso", "torso"),
				 ("waist", "waist"),
				 ("feet", "feet")])
	armor_bonus = IntegerField('Armor Bonus', validators=[Optional(), NumberRange(min=0)])
	max_dex_bonus = IntegerField('Max Dex Bonus', validators=[Optional(), NumberRange(min=0)])
	armor_check_penalty = IntegerField('Armor Check Penalty', validators=[Optional(), NumberRange(max=0)]) #negative numbers
	arcane_spell_failure = IntegerField('Arcane Spell Failure', validators=[Optional(), NumberRange(min=0, max=100)]) #in %
	movement_speed = IntegerField('Movement Speed', description="For creatures with a normal movement speed of 30 ft.", validators=[Optional(), NumberRange(min=0)])
	
	#miscellaneous features
	total_uses = IntegerField('Total Uses', validators=[Optional(), NumberRange(min=0)])
	attribute_modifiers = FieldList(FormField(AttributeModForm), 'Attribute Modifiers', validators=[Optional()])
	relevant_spells = FieldList(StringField('Relevant Spell', validators=[Regexp('^[A-Za-z ]+$', 0, 'Lowercase letters only.')]), validators=[Optional()])
	description = TextAreaField('Description', validators=[Optional()])
	submit = SubmitField('Submit')



		