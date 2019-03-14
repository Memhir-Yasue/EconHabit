import flask
import db
from flask import Flask
from Ecop import Ecop

server = flask.Flask(__name__)

Halowa = Ecop(10)
GDP = str(db.fetch_last_gdp())
@server.route('/')
def main():
    return GDP

if __name__ == '__main__':
    server.run(debug=True)
