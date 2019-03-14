import sqlite3
import os.path
import time


def startdb():
    global conn, cursor
    conn = sqlite3.connect('ecoHabit.db')
    cursor = conn.cursor()

def closedb():
    cursor.close()
    conn.close()

def connect():
    cursor.execute("CREATE TABLE IF NOT EXISTS econData(unixTime REAL, GDP REAL)")

def data_entry(GDP):
    unix = time.time()
    cursor.execute("INSERT INTO econData (unixTime, GDP) VALUES(?,?)",
    (unix, GDP))
    conn.commit()

def fetch_last_gdp():
    startdb()
    cursor.execute("SELECT * FROM econData ORDER BY GDP DESC LIMIT 1")
    result = cursor.fetchone()
    return result[1]

def db_exists():
    os.path.exists("ecoHabit.db")
