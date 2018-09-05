import pymongo
from .fields import Field

class ModelBase(type):
	"""
		classes using this metaclass will have the following attrs
			-- objects an instance of _db
			-- field_name an instance of Field class
			-- _data a dict with field_name as key and
				 Field instance as value
	"""

	# control the creation of a class whose metaclass is this 
	# class, by overriding the "__new__" method of the "type" 
	# metaclass
	def __new__(cls, clsname, bases, clsdict):
		# create a class using the "__new__" magic method of the
		# type metaclass
		new_class = super().__new__(cls, clsname, bases, clsdict)


		# here we add our custom code injuctions
		# create a database instance
		DB_URI = "mongodb://127.0.0.1:27017"
		client = pymongo.MongoClient(DB_URI)

		_db = client['true_buyers']

        # add objects attribute with a database instance to our class
		new_class.add_to_class('objects', _db)

		# loop over the class dicts (attributes and methods)
        # check if all attributes are an instance of our 
        # Fidld class
		for field_name, field in clsdict.items():
			if(isinstance(field, Field)):
        		# set the _name attr of field instance to
        		# field_name
				field._name = field_name
				new_class.add_to_class(field_name, field)
			# else:
				# raise TypeError('All fields shoule be an instance of Field class!!!')

        # create a dict of field name and field value if field in an 
        # instance of Field class
		data = dict(((key, item) for key, item in clsdict.items() if isinstance(item, Field)))
		
		# for key, item in data.items():
		# 	print(key +'======='+str(type(item)))


		# add data dict to _data attribute
		new_class.add_to_class('_data', data) 
		return new_class       

	def add_to_class(cls, name, value):
		setattr(cls, name, value)


class Model(metaclass=ModelBase):
	"""
	The class that all our models inherite. this class have the
	following methodes
		-- __init__
		-- save
		-- error_messages
	Note: we can access all the attributes from the metaclass ModelBase
	by using self.
	"""
	# init class for our models to inherite
	def __init__(self,):
		self.errors = []
		self.data = {}
		# Make objects point to the colletcion with the class name
		self.objects = self.objects[type(self).__name__.lower()]
		# If we make objects an instance of a more complex class
		# with pymongo methodes, create, save, --- we will make our
		# Model class comparable to DJANGO.


	def create(self, **kwargs): 
		# Ex book = Book().create(title='django'), then add that to the
		# _data dict attr by setting _data['title']: <class Filed>
		# to _data['title']: 'django'
		for item in self._data:
			if item in kwargs:
				# get the model.field_name and set it
				getattr(self, item).set(kwargs[item])
				# print('{} = {}'.format(item, self._data[item]))
			else:
				# getattr(self, item).set()
				raise TypeError('Undefind field given to create model!!!')


	def save(self):
		valid = True
		for item in self._data:
			# Get the Field value stared in the attr of the class and call the 
			# Validate() method on
			valid = valid if getattr(self, item).validate() else False
			if not valid:
				self.errors = getattr(self, item)
				break
			# ORM change the mode to db frendly format
			self.data[item] = getattr(self, item).get()
		# First time validate return false the operation will break out of
		# the loop
		if valid:
			try:
				return self.objects.insert(self.data)
			except Exceptions as e:
				print(e)
		else:
			raise TypeError(self.errors)
			return self.errors


	def error_messages(self):
		return self.errors.join('\n')
