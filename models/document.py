import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from database import Base

class document(Base):
    __tablename__ = 'picdocument'
    pdocid = Column(Integer, primary_key=True)

    title = Column(String(80), unique=True)
    text = Column(String(120))
    docpath = Column(String(120))
    picno = Column(Integer)
    picname = Column(String(120))
    picmid = Column(Integer)

    def __init__(self):
        pass

    def __repr__(self):
        return '<title %r>' % (self.title)
