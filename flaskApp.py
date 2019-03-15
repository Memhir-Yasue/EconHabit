import flask
import db
from flask import Flask, render_template, request
from Ecop import Ecop

def initalizeDB():
    print(db.db_exists())
    if(db.db_exists()):
        GDP = db.fetch_last_gdp()
        print("EXISTS!")
        return GDP
    else:
        db.startdb()
        db.connect()
        GDP = 10
        db.data_entry(GDP)
        db.closedb()
        return GDP


GDP = initalizeDB()
Account = Ecop(GDP)

server = flask.Flask(__name__)
#
# Halowa = Ecop(10)
# GDP = str(db.fetch_last_gdp())
@server.route('/')
def home():
    return render_template('index.html', GDP = GDP)

@server.route('/', methods=['POST'])
def update():
    state = request.form['state']
    Account.state(int(state))
    Account.calculate()
    GDP = str(Account.gdp_size())
    db.startdb()
    db.connect()
    db.data_entry(GDP)
    db.closedb()
    print(GDP)
    return render_template('index.html', GDP = GDP)

# @server.route('/u', methods=['POST'])
# def update():
#     state = request.form['state']
#     Account.state(state)
#     Account.calculate()
#     GDP = str(Account.gdp_size())
#     db.data_entry(GDP)
#     return render_template('test.html', GDP = GDP)

if __name__ == '__main__':
    server.run(debug=True)
