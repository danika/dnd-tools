from flask.ext.wtf import Form
from wtforms import *
from wtforms.validators import *

class SignUpForm(Form):
	email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
	name = StringField('Name', validators=[DataRequired(), Length(1,64), 
		Regexp('^[A-Za-z ]+$', 0, 'Names must have only letters and spaces.')])
	pwd1 = PasswordField('Password', validators=[DataRequired(), Length(6,20)])
	pwd2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('pwd1','Passwords must match.')])
	signup = SubmitField('Sign Up')


class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired(), Length(1,64)])
	pwd = PasswordField('Password', validators=[DataRequired()])
	login = SubmitField('Login')

class WeaponDamageForm(Form):
	dmg_type = StringField('Damage Type', 
		validators=[Regexp('^[A-Za-z ]+$', 0, 'Lowercase letters only.')])
	amount = StringField('Amount')

class AddItemForm(Form):
	#required features
	name = StringField('Item Name', validators=[DataRequired()])
	reference = StringField('Reference', validators=[DataRequired()])
	weight = DecimalField('Weight', validators=[DataRequired(), NumberRange(min=0)], places=1)
	value = DecimalField('Value', validators=[DataRequired(), NumberRange(min=0)], places=2)
	#item_type = StringField('Item Type', validators=[DataRequired()])
	
	#weapon features
	weapon_types = FieldList(StringField('Weapon Type', 
		validators=[Regexp('^[A-Za-z ]+$', 0, 'Lowercase letters only.')]))
	damage = FieldList(FormField(WeaponDamageForm), 'Damage')
	
	critical = StringField('Critical')
	range_increment = IntegerField('Range', min=) #in ft
	#armor features
	armor_type = TextField()
	armor_bonus = IntegerField()
	max_dex_bonus = IntegerField()
	armor_check_penalty = IntegerField()
	arcane_spell_failure = IntegerField() #in %
	movement_speed = IntegerField()
	#miscellaneous features
	total_uses = IntegerField()
	bonuses = ListField(DictField(Mapping.build(
							quality = TextField(),
							modifier = TextField())))
	#[{"quality":"listen", "modifier":"+2"}, {"quality":"spot", "modifier":"+2"}]
	
	relevant_spells = ListField(TextField()) #["comprehend languages", "read magic"]
	description = TextField()
		