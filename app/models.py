import couchdb
from couchdb.mapping import *
from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

#------DB Setup------
server = couchdb.Server()
users_db = server['dnd_users']
items_db = server['dnd_items']

class User(UserMixin, Document):
	email = TextField()
	name = TextField()
	password_hash = TextField()

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

class Character(Document):
	name = TextField()
	inventory = ListField(DictField(Mapping.build(
							item = TextField(), #item id
							quantity = IntegerField(),
							notes = TextField())))

class Item(Document):
	#required features
	name = TextField()
	reference = TextField() #this will become a more complicated field later on
	weight = DecimalField() #in lbs
	value = DecimalField() #in gold
	#item_type = TextField()
	#weapon features
	weapon_types = ListField(TextField()) #["simple", "light", "melee"]
	damage = ListField(DictField(Mapping.build(
							dmg_type = TextField(),
							amount = TextField())))
	#[{"type": "piercing", "amount": "1d6"}, {"type":"fire", "amount":"1d6"}]
	
	critical = TextField()
	range_increment = IntegerField() #in ft
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





