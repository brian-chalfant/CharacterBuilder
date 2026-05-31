import sqlite3
from pathlib import Path

import json

home = str(Path.home())
DB_PATH = Path(__file__).resolve().parent / 'CharacterBuilder.db'


def write_background():
    data = []
    NAME = input("Name: ")
    data.append(NAME)
    SKILLPROF = input("SkillProf: ")
    data.append(SKILLPROF)
    LANGUAGES = input("Languages: ")
    data.append(LANGUAGES)
    TOOLS = input("Tools: ")
    data.append(TOOLS)
    EQUIPMENT = input("Equipment: ")
    data.append(EQUIPMENT)
    FEATURE = input("Feature: ")
    data.append(FEATURE)
    FEATDESC = input("Feature Description: ")
    PERSTRAIT1 = input("PERSTRAIT1: ")
    data.append(PERSTRAIT1)
    PERSTRAIT2 = input("PERSTRAIT2: ")
    data.append(PERSTRAIT2)
    PERSTRAIT3 = input("PERSTRAIT3: ")
    data.append(PERSTRAIT3)
    PERSTRAIT4 = input("PERSTRAIT4: ")
    data.append(PERSTRAIT4)
    PERSTRAIT5 = input("PERSTRAIT5: ")
    data.append(PERSTRAIT5)
    PERSTRAIT6 = input("PERSTRAIT6: ")
    data.append(PERSTRAIT6)
    PERSTRAIT7 = input("PERSTRAIT7: ")
    data.append(PERSTRAIT7)
    PERSTRAIT8 = input("PERSTRAIT8: ")
    data.append(PERSTRAIT8)
    IDEAL1 = input("IDEAL1: ")
    data.append(IDEAL1)
    IDEAL2 = input("IDEAL2: ")
    data.append(IDEAL2)
    IDEAL3 = input("IDEAL3: ")
    data.append(IDEAL3)
    IDEAL4 = input("IDEAL4: ")
    data.append(IDEAL4)
    IDEAL5 = input("IDEAL5: ")
    data.append(IDEAL5)
    IDEAL6 = input("IDEAL6: ")
    data.append(IDEAL6)
    BOND1 = input("BOND1: ")
    data.append(BOND1)
    BOND2 = input("BOND2: ")
    data.append(BOND2)
    BOND3 = input("BOND3: ")
    data.append(BOND3)
    BOND4 = input("BOND4: ")
    data.append(BOND4)
    BOND5 = input("BOND5: ")
    data.append(BOND5)
    BOND6 = input("BOND6: ")
    data.append(BOND6)
    FLAW1 = input("FLAW1: ")
    data.append(FLAW1)
    FLAW2 = input("FLAW2: ")
    data.append(FLAW2)
    FLAW3 = input("FLAW3: ")
    data.append(FLAW3)
    FLAW4 = input("FLAW4: ")
    data.append(FLAW4)
    FLAW5 = input("FLAW5: ")
    data.append(FLAW5)
    FLAW6 = input("FLAW6: ")
    data.append(FLAW6)
    print(data)
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('INSERT INTO backgrounds (NAME, SKILLPROF, LANGUAGES, TOOLS, EQUIPMENT, FEATURE, FEATDESC, '
                'PERSTRAIT1, PERSTRAIT2, PERSTRAIT3, PERSTRAIT4, PERSTRAIT5, PERSTRAIT6, '
                'PERSTRAIT7, PERSTRAIT8, IDEAL1, IDEAL2, IDEAL3, IDEAL4, IDEAL5, IDEAL6, BOND1, '
                'BOND2, BOND3, BOND4, BOND5, BOND6, FLAW1, FLAW2, FLAW3, FLAW4, FLAW5, FLAW6) VALUES '
                '(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (NAME, SKILLPROF, LANGUAGES, TOOLS, EQUIPMENT, FEATURE, FEATDESC,
                 PERSTRAIT1, PERSTRAIT2, PERSTRAIT3, PERSTRAIT4, PERSTRAIT5, PERSTRAIT6,
                 PERSTRAIT7, PERSTRAIT8, IDEAL1, IDEAL2, IDEAL3, IDEAL4, IDEAL5, IDEAL6,
                 BOND1, BOND2, BOND3, BOND4, BOND5, BOND6, FLAW1, FLAW2, FLAW3, FLAW4, FLAW5, FLAW6))
    conn.commit()
    conn.close()


def read_backgrounds(name):
    data = ['NAME', 'SKILLPROF', 'LANGUAGES', 'TOOLS', 'EQUIPMENT', 'FEATURE', 'FEATDESC', 'PERSTRAIT1', 'PERSTRAIT2',
                    'PERSTRAIT3', 'PERSTRAIT4', 'PERSTRAIT5', 'PERSTRAIT6', 'PERSTRAIT7', 'PERSTRAIT8', 'IDEAL1',
                    'IDEAL2', 'IDEAL3', 'IDEAL4', 'IDEAL5', 'IDEAL6', 'BOND1', 'BOND2', 'BOND3', 'BOND4',
                    'BOND5', 'BOND6', 'FLAW1', 'FLAW2', 'FLAW3', 'FLAW4', 'FLAW5', 'FLAW6']
    rtndict = {}
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('SELECT * FROM backgrounds WHERE NAME = ?', (name,))

    x = cur.fetchall()
    conn.close()
    for j in range(len(data)):
        rtndict[data[j]] = x[0][j]

    return rtndict


def read_background_names():
    rtndict = {}
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('SELECT NAME FROM backgrounds')

    x = cur.fetchall()
    conn.close()

    for i in range(len(x)):
        rtndict[i+1] = x[i][0]
    return rtndict


def multi_write():
    done = False
    while done is not True:
        write_background()
        a = (input('Done? (y/n)'))
        if a.lower() == 'y':
            done = True
        if a.lower() == 'n':
            done = False
