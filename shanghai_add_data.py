import sqlite3

conn = sqlite3.connect('shanghai.db')
cursor = conn.cursor()

cursor.execute("INSERT INTO ACCOUNT (ID, ACCOUNT) VALUES (1, 10000.00 )")

conn.commit()
conn.close()