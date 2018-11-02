import sqlite3
from build_sheet import string_format

def read_features(name):
    conn = sqlite3.connect('CharacterBuilder.db')
    cur = conn.cursor()

    cur.execute('SELECT description FROM features WHERE NAME = \"{na}\"'.format(na=name))

    x = cur.fetchall()
    conn.close()

    return name + ": " + x[0][0]



if __name__ == '__main__':
    x = read_features('RAGE')
    for i in string_format(x):
        print(i)