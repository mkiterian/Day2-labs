class Car():

	def __init__(self, name='General', model='GM', car_type='saloon'):
		self.car_type = car_type
		self.model = model
		self.name = name
		self.speed = 0

		if self.name == 'Porshe' or self.name =='Koenigsegg':
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4 

		if self.car_type == 'trailer':
			self.num_of_wheels = 8
		else: 
			self.num_of_wheels = 4

	def is_saloon(self):
		if self.car_type != 'trailer':
			return True
		else:
			return False

	def drive(self, acc):
		if acc == 7:
			self.speed = 77
		elif acc == 3:
			self.speed = 1000
		return self


