import flask
import db
from flask import Flask
from Ecop import Ecop

def initalizeDB():
    if(db.db_exists()):
        GDP = db.fetch_last_gdp()
        return GDP
    else:
        Halowa = Ecop(10)
        db.startdb()
        db.connect()
        GDP = Halowa.gdp_size()
        db.data_entry(GDP)
        GDP = db.fetch_last_gdp()
        print(GDP)
        db.closedb()
        return GDP


server = flask.Flask(__name__)
#
# Halowa = Ecop(10)
# GDP = str(db.fetch_last_gdp())
@server.route('/')
def main():
    GDP = initalizeDB()
    return str(GDP)

if __name__ == '__main__':
    server.run(debug=True)
