import sqlite3
from pathlib import Path

import json

home = str(Path.home())


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
    conn = sqlite3.connect('background.db')
    cur = conn.cursor()

    cur.execute('INSERT INTO backgrounds (NAME, SKILLPROF, LANGUAGES, TOOLS, EQUIPMENT, FEATURE, FEATDESC, '
                'PERSTRAIT1, PERSTRAIT2, PERSTRAIT3, PERSTRAIT4, PERSTRAIT5, PERSTRAIT6, '
                'PERSTRAIT7, PERSTRAIT8, IDEAL1, IDEAL2, IDEAL3, IDEAL4, IDEAL5, IDEAL6, BOND1, '
                'BOND2, BOND3, BOND4, BOND5, BOND6, FLAW1, FLAW2, FLAW3, FLAW4, FLAW5, FLAW6) VALUES '
                '( \"{na}\",\"{sp}\",\"{la}\",\"{tl}\", \"{eq}\",\"{fe}\",\"{fd}\",\"{p1}\",\"{p2}\",\"{p3}\",\"{p4}\",'
                '\"{p5}\",\"{p6}\",\"{p7}\",\"{p8}\",\"{i1}\",\"{i2}\",\"{i3}\",\"{i4}\",\"{i5}\",\"{i6}\",\"{b1}\",'
                '\"{b2}\",\"{b3}\",\"{b4}\",\"{b5}\",\"{b6}\",\"{f1}\",\"{f2}\",\"{f3}\",\"{f4}\",\"{f5}\",\"{f6}\" )'
                .format(na=NAME, sp=SKILLPROF, la=LANGUAGES,
                        tl=TOOLS, fe=FEATURE, fd=FEATDESC, eq=EQUIPMENT,
                        p1=PERSTRAIT1, p2=PERSTRAIT2,p3=PERSTRAIT3,
                        p4=PERSTRAIT4, p5=PERSTRAIT5, p6=PERSTRAIT6,
                        p7=PERSTRAIT7, p8=PERSTRAIT8, i1=IDEAL1,
                        i2=IDEAL2, i3=IDEAL3, i4=IDEAL4, i5=IDEAL5,
                        i6=IDEAL6, b1=BOND1, b2=BOND2,
                        b3=BOND3, b4=BOND4, b5=BOND5,
                        b6=BOND6, f1=FLAW1, f2=FLAW2,
                        f3=FLAW3, f4=FLAW4, f5=FLAW5, f6=FLAW6))
    conn.commit()
    conn.close()


def read_backgrounds(name):
    data = ['NAME', 'SKILLPROF', 'LANGUAGES', 'TOOLS', 'EQUIPMENT', 'FEATURE', 'FEATDESC', 'PERSTRAIT1', 'PERSTRAIT2',
                    'PERSTRAIT3', 'PERSTRAIT4', 'PERSTRAIT5', 'PERSTRAIT6', 'PERSTRAIT7', 'PERSTRAIT8', 'IDEAL1',
                    'IDEAL2', 'IDEAL3', 'IDEAL4', 'IDEAL5', 'IDEAL6', 'BOND1', 'BOND2', 'BOND3', 'BOND4',
                    'BOND5', 'BOND6', 'FLAW1', 'FLAW2', 'FLAW3', 'FLAW4', 'FLAW5', 'FLAW6']
    rtndict = {}
    conn = sqlite3.connect('background.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM backgrounds WHERE NAME = \"{na}\"'.format(na=name))

    x = cur.fetchall()
    conn.close()
    for j in range(len(data)):
        rtndict[data[j]] = x[0][j]

    return rtndict


def read_background_names():
    rtndict = {}
    conn = sqlite3.connect('background.db')
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
