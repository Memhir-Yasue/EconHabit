from Ecop import Ecop


Halowa = Ecop(10)

Halowa.state(1)
for i in range(100):
	Halowa.calculate()
print(Halowa.gdp_size())