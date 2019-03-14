import db
from Ecop import Ecop


Halowa = Ecop(10)
db.startdb()
db.connect()
Halowa.state(1)
for i in range(100):
	Halowa.calculate()
	GDP = Halowa.gdp_size()
	db.data_entry(GDP)
db.closedb()
