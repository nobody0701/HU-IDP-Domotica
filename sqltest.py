import psycopg2

try:
    conn = psycopg2.connect("dbname='OV' user='postgres' host='localhost' password='0000'")
    cur = conn.cursor()

    cur.execute("""SELECT * FROM adres""")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.commit()

    cur.close()

except psycopg2.OperationalError:
    print("[Database] I am unable to connect to the database")

# rows = cur.fetchall()
# for row in rows:
#     print(row)
