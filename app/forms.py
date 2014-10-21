from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FieldList, FormField, TextAreaField, SelectField
from wtforms import Form as NoCSRFForm
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


class TextSearchForm(Form):
	field_choice = SelectField('Choice', 
		choices=[("name", "name"),
				("book", "book"),
				("critical", "critical"),
				("armor_type", "armor type"),
				("body_slot", "body slot"),
				("description", "description")])
	operator_choice = SelectField('Operator', 
		choices=[("exactly like", "exactly like"),
				("similar_to", "similar to")])
	user_input = StringField('Input')

class NumberSearchForm(Form):
	field_choice = SelectField('Choice', 
		choices=[("weight", "weight"),
				("value", "value"),
				("range_increment", "range increment"),
				("armor_bonus", "armor bonus"),
				("max_dex_bonus", "max dex bonus"),
				("armor_check_penalty", "armor check penalty"),
				("arcane_spell_failure", "arcane spell failure"),
				("movement_speed", "movement speed")])
	operator_choice = SelectField('Operator', 
		choices=[("equals", "="),
				("greater_than", ">"),
				("less_than", "<")])
	user_input = DecimalField('Input')


class BrowseForm(Form):
	text_searches = FieldList(FormField(TextSearchForm), 'Text', validators=[Optional()], min_entries=1)
	number_searches = FieldList(FormField(NumberSearchForm), 'Numbers', validators=[Optional()], min_entries=1)
	submit = SubmitField('Search')


class ReferenceForm(NoCSRFForm):
	book = StringField('Book', validators=[InputRequired(message='Must enter a reference book.')])
	page = StringField('Page', validators=[InputRequired(message='Must enter a reference page.')])

class WeaponTypesForm(NoCSRFForm):
	unarmed = BooleanField('unarmed', validators=[Optional()])
	light = BooleanField('light', validators=[Optional()])
	melee = BooleanField('melee', validators=[Optional()])
	one_handed = BooleanField('one-handed', validators=[Optional()])
	two_handed = BooleanField('two-handed', validators=[Optional()])
	ranged = BooleanField('ranged', validators=[Optional()])
	simple = BooleanField('simple', validators=[Optional()])
	martial = BooleanField('martial', validators=[Optional()])
	exotic = BooleanField('exotic', validators=[Optional()])

class WeaponDamageForm(NoCSRFForm):
	dmg_type = StringField('Type', 
		validators=[Optional(), Regexp('^[a-z ]+$', 0, 'Lowercase letters and spaces only.')])
	amount = StringField('Amount')

class AttributeModForm(NoCSRFForm):
	attribute = StringField('Attribute', validators=[Regexp('^[a-z ]+$', 0, 'Lowercase letters and spaces only.')])
	modifier = IntegerField('Modifier')

class AddItemForm(Form):
	#required features
	name = StringField('Name', validators=[InputRequired()])
	references = FieldList(FormField(ReferenceForm), 'References', min_entries=1)
	weight = DecimalField('Weight', validators=[InputRequired(), NumberRange(min=0)], places=2)
	value = DecimalField('Value', validators=[InputRequired(), NumberRange(min=0)], places=2)
	
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
				 ("other", "other")])
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
	movement_speed = IntegerField('Movement Speed', description="(For creatures with a normal movement speed of 30 ft.)", validators=[Optional(), NumberRange(min=0)])
	
	#miscellaneous features
	attribute_modifiers = FieldList(FormField(AttributeModForm), 'Attribute Modifiers', validators=[Optional()])
	total_uses = IntegerField('Total Uses', validators=[Optional(), NumberRange(min=0)])
	description = TextAreaField('Description', validators=[Optional()])
	submit = SubmitField('Submit')



		