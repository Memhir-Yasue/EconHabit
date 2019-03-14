import random
from datetime import datetime


class Ecop:
	"""docstring for Ecop"""


	def __init__(self, economy):
		self.economy = economy

	def state(self, choice):
		self.choice = choice

	def gdp_size(self):
		return round(self.economy,2)

	def compound(self, growth):
		principle = self.gdp_size()
		return principle * (1 + growth)


	def calculate(self):
		random.seed(datetime.now())
		forcast = random.randint(0, 102)
		principle = self.gdp_size()
		if self.choice == 1:
			if(forcast >= 1 and forcast < 6):
				growth = (random.randint(-1,3)) * 1/100
				self.economy = self.compound(growth)
				return round(self.economy,2) # round two decimal places

			elif(forcast >= 6 and forcast < 21):
				growth = (random.randint(3,5)) * 1/100
				self.economy = self.compound(growth)
				return round(self.economy,2)

			elif(forcast >= 21 and forcast < 71):
				growth = (random.randint(5,7)) * 1/100
				self.economy = self.compound(growth)
				return round(self.economy,2)

			elif(forcast >= 70 and forcast < 96):
				growth = (random.randint(7,10)) * 1/100
				self.economy = self.compound(growth)
				return round(self.economy,2)

			elif(forcast >= 96 and forcast < 101):
				growth = (random.randint(10,13)) * 1/100
				self.economy = self.compound(growth)
				return round(self.economy,2)
		else:
			if self.choice == 0:
				if(forcast >= 1 and forcast < 6):
					growth = (random.randint(-1,0)) * 1/100
					self.economy = self.compound(growth)
					return round(self.economy,2)

				elif(forcast >= 6 and forcast < 21):
					growth = (random.randint(-3,-1)) * 1/100
					self.economy = self.compound(growth)
					return round(self.economy,2)

				elif(forcast >= 21 and forcast < 71):
					growth = (random.randint(-6,-3)) * 1/100
					self.economy = self.compound(growth)
					return round(self.economy,2)

				elif(forcast >= 70 and forcast < 96):
					growth = (random.randint(-9,-6)) * 1/100
					self.economy = self.compound(growth)
					return round(self.economy,2)

				elif(forcast >= 96 and forcast < 101):
					growth = (random.randint(-12,-9)) * 1/100
					self.economy = self.compound(growth)
					return round(self.economy,2)
