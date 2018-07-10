from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import category,document, picfile
from database import db_session

def insertCategory():

    for c in category.piccategory.query.all():
        print("about to delete categoryPic:",c.title)
        db_session.delete(c)
        db_session.commit()



    for i in range(10):
        cate = category.piccategory()
        cate.title = str(i)+":"+"testInsert"
        cate.text = 47121 * i
        cate.categorypath = "cate/"+str(i)
        db_session.add(cate)
        print(cate)
        print(cate.title)
        print(cate.pcateid)
    db_session.commit()

insertCategory()
