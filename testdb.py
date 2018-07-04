import sqlite3

conn = sqlite3.connect('tmp/flaskr.db')

c = conn.cursor()
c.execute('select * from piccategory')

print(c.fetchall())
