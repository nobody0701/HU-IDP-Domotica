import psycopg2
import time
from datetime import *

def Status(id):
    verzenddict = {}
    #id = 1
    conn = psycopg2.connect("dbname='idp' user='postgres' host='localhost' password='0000'")
    cur = conn.cursor()

    cur.execute("SELECT kamer.*, stofzuiger.*, gordijnen.*, alarm.* FROM kamer, stofzuiger, gordijnen, alarm WHERE kamer.kamerid = " + str(id) + ";")

    rows = cur.fetchall()
    now = datetime.now()
    now_time = now.time()
    datebasestarttime = (rows[0][4])
    datebaseendtime = (rows[0][5])
    gordijnopen = (rows[0][8])
    gordijnsluit = (rows[0][9])
    alarmaan = (rows[0][12])
    alarmuit = (rows[0][13])

    if datebasestarttime <= now_time <= datebaseendtime:
        verzenddict.update({'stofzuiger': True})
        if rows[0][6] == 'nee':
            cur.execute("UPDATE stofzuiger SET actief = 'ja' WHERE kamerid = " + str(id) + ";")
    else:
        verzenddict.update({'stofzuiger': False})
        if rows[0][6] == 'ja':
            cur.execute("UPDATE stofzuiger SET actief = 'nee' WHERE kamerid = " + str(id) + ";")
    if gordijnopen <= now_time <= gordijnsluit:
        verzenddict.update({'gordijnen': True})
        if rows[0][10] == 'nee':
            cur.execute("UPDATE gordijnen SET gordijnopen = 'ja' WHERE kamerid = " + str(id) + ";")
    else:
        verzenddict.update({'gordijnen': False})
        if rows[0][10] == 'ja':
            cur.execute("UPDATE gordijnen SET gordijnopen = 'nee' WHERE kamerid = " + str(id) + ";")
    if alarmaan <= now_time <= alarmuit:
        verzenddict.update({'infrarood': True})
        if rows[0][13] == 'nee':
            cur.execute("UPDATE alarm SET actief = 'ja' WHERE kamerid = " + str(id) + ";")
    else:
        verzenddict.update({'infrarood': False})
        if rows[0][13] == 'ja':
            cur.execute("UPDATE alarm SET actief = 'nee' WHERE kamerid = " + str(id) + ";")

    conn.commit()

    cur.close()

    return verzenddict

def lezenstatus(data, id):
    data = eval(data)
    if str(data) == str('none'):
        return
    else:
        datakeys = list(data.keys())
        for x in datakeys:
            if data[x][0] == 'melding':
                conn = psycopg2.connect("dbname='idp' user='postgres' host='localhost' password='0000'")
                cur = conn.cursor()
                cur.execute("SELECT * FROM meldingen")
                row = cur.fetchall()
                if row == []:
                    cur.execute("INSERT INTO meldingen(kamerid, meldingtekst) VALUES (" + id + ", '" + str(data[x][1]) + "');")
                    print('aangemaakt')
                else:
                    napa = True
                    for a in row:
                        if str(a[0]) == str(id) and str(a[1]) == str(data[x][1]):
                            napa = False
                            break
                    if napa:
                        cur.execute("INSERT INTO meldingen(kamerid, meldingtekst) VALUES (" + id + ", '" + str(data[x][1]) + "');")
                        print("aangemaakt")
                conn.commit()
                cur.close()

def verbindingverloren(idaa):
    conn = psycopg2.connect("dbname='idp' user='postgres' host='localhost' password='0000'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM meldingen")
    row = cur.fetchall()
    if row == []:
        cur.execute("INSERT INTO meldingen(kamerid, meldingtekst) VALUES (" + idaa + ", 'Connect lost');")
        print('aangemaakt')
    else:
        napa = True
        for a in row:
            if str(a[0]) == str(idaa) and str(a[1]) == str('Connect lost'):
                napa = False
                break
        if napa:
            cur.execute("INSERT INTO meldingen(kamerid, meldingtekst) VALUES (" + idaa + ", 'Connect lost');")
            print("aangemaakt")
    conn.commit()
    cur.close()
