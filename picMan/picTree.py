import os
import sqlite3
from flask import current_app

class picTree:

    def __init__(self, app=None):
      self.app = app
      
    def GetCategory(self,cate=None, size=20, num=0):
        conn = self.connect_db()
        c = conn.cursor()
        sql = "select * from piccategory"# order by title limit "+str(num*size)+" offset "+str(size)
        print(sql)
        c.execute(sql)
        list = c.fetchall()
        print(list)
        c.close()
        return list

    def connect_db(self):
        print(os.path.abspath(current_app.config['DATABASE']))
        return sqlite3.connect(current_app.config['DATABASE'])
        
    def AddCategory(self,title=None,text=None,picpath=None):        
        conn = self.connect_db()
        c = conn.cursor()
        sql = "INSERT INTO piccategory (title,text,categorypath) VALUES (:TITLE,:TEXT,:PATH)"
        c.execute(sql,{"TITLE":title,"TEXT":text,"PATH":picpath})
        conn.commit()
        print('insert')
        print(title,text,picpath)
        c.close()
        conn.close()