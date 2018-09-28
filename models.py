from db.models import Model
from db import fields


class Purchases(Model):
	user_id = fields.CharField()
	user_name = fields.CharField()
	purchase_from = fields.CharField()
	name = fields.CharField()
	picture = fields.CharField()
	price = fields.FloatField()
	store_name = fields.CharField()
	store_location = fields.CharField()
	condition = fields.CharField()
	genuine = fields.BooleanField()
	rating = fields.IntegerField()
	review = fields.CharField()
	recommend = fields.BooleanField()
	gps = fields.BooleanField()
	latitude = fields.FloatField()
	longitude = fields.FloatField()
	shared = fields.BooleanField()
	supercategory = fields.CharField()
	category = fields.CharField()
	reactors = fields.ListField()
	# date = fields.DateField()
