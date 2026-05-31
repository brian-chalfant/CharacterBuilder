import sqlite3
from pathlib import Path
from build_sheet import string_format

DB_PATH = Path(__file__).resolve().parent / 'CharacterBuilder.db'

def read_features(name):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('SELECT description FROM features WHERE NAME = ?', (name,))

    x = cur.fetchall()
    conn.close()

    return name + ": " + x[0][0]



if __name__ == '__main__':
    x = read_features('RAGE')
    for i in string_format(x):
        print(i)