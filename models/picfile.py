import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from database import db

class picfile(db.Model):
    __tablename__ = 'picfile'
    id = Column(Integer, primary_key=True)
    pdocid = Column(Integer)
    fileno = Column(Integer)

    md5code = Column(String(120))
    fpath = Column(String(120))


    #for flask-sqlalchemy reason , 不实现init
    def __init__(self):
        pass


    def __repr__(self):
        return '<title %r>' % (self.title)
