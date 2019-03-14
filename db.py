import sqlite3
import time


def startdb():
    global conn, cursor
    conn = sqlite3.connect('ecoHabit.db')
    cursor = conn.cursor()

def closedb():
    cursor.close()
    conn.close()

def connect():
    startdb()
    cursor.execute("CREATE TABLE IF NOT EXISTS econData(unixTime REAL, GDP REAL)")

def data_entry(GDP):
    unix = time.time()
    cursor.execute("INSERT INTO econData (unixTime, GDP) VALUES(?,?)",
    (unix, GDP))
    conn.commit()
