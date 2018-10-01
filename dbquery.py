import sqlite3


def dbconnect(db_file):
    conn = sqlite3.connect(db_file)
    return conn


