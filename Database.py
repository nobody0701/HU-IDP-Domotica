import psycopg2

def data(datatype):
    try:
        conn = psycopg2.connect("dbname='idp' user='postgres' host='localhost' password='0000'")
        cur = conn.cursor()
        if datatype != str:
            if datatype == 0:
                cur.execute("SELECT a.naambewoner, b.* FROM kamer a, meldingen b WHERE a.kamerid = b.kamerid;")
            if datatype == 1:
                cur.execute("SELECT naambewoner FROM kamer")
            if datatype == 2:
                cur.execute("SELECT a.*, b.*, c.* FROM kamer a, stofzuiger b, gordijnen c WHERE a.kamerid = b.kamerid AND a.kamerid = c.kamerid;")
            rows = cur.fetchall()
            cur.close()
            return rows

    except psycopg2.OperationalError:
        print("I am unable to connect to the database")

def dataremove(data1, data2):
    try:
        conn = psycopg2.connect("dbname='idp' user='postgres' host='localhost' password='0000'")
        cur = conn.cursor()
        cur.execute("DELETE FROM meldingen WHERE kamerid = " + data1 + " AND meldingtekst = '" + data2 + "';")

        conn.commit()

        cur.close()
    except psycopg2.OperationalError:
        print("I am unable to connect to the database")

def datawijzigen(data1, data2):
    try:
        conn = psycopg2.connect("dbname='idp' user='postgres' host='localhost' password='0000'")
        cur = conn.cursor()
        cur.execute("UPDATE gordijnen SET opentijd = '" + data1 + "' WHERE kamerid = " + data2 + ";")

        conn.commit()

        cur.close()
    except psycopg2.OperationalError:
        print("I am unable to connect to the database")

def datawijzigen1(data1, data2, data3):
    try:
        conn = psycopg2.connect("dbname='idp' user='postgres' host='localhost' password='0000'")
        cur = conn.cursor()
        cur.execute("UPDATE stofzuiger SET starttijd = '" + data1 + "', stoptijd = '" + data2 + "' WHERE kamerid = " + data3 + ";")
        #cur.execute("UPDATE stofzuiger SET stoptijd = '" + data2 + "' WHERE kamerid = " + data3 + ";")

        conn.commit()

        cur.close()
    except psycopg2.OperationalError:
        print("I am unable to connect to the database")
