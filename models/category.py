import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from database import db

class piccategory(db.Model):
    __tablename__ = 'piccategory'
    pcateid = Column(Integer, primary_key=True)

    title = Column(String(80), unique=True)
    text = Column(String(120))
    categoryno = Column(String(120))
    categoryname = Column(String(120))
    categoryurl = Column(String(120))
    tags = Column(String(120))


    def __init__(self):
        print("-----base------")
        #print(Base)
        pass


    def __repr__(self):
        return '<piccategory %r>' % (self.title)

    def testBase(self):
        print("-----base------")
        print(Base)
