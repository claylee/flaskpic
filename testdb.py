import sqlite3
from pprint import pprint

conn = sqlite3.connect('tmp/flaskr.db')

c = conn.cursor()

sql = 'select * from sqlite_master where type="table"'
c.execute(sql)
for i in c.fetchall():
    pprint(i)

c.execute('select * from piccategory')
pprint(c.fetchall())

c.execute('select * from picdocument')
pprint(c.fetchall())

c.execute('select * from picfile')
pprint(c.fetchall())

conn.close()
