# all the imports
import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from config import Config
from contextlib import closing

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from pprint import pprint

from database import db_session

import views

app = Flask(__name__)

app.config.from_object(Config)

pprint(app.config)


@app.teardown_request
def shutdown_session(exception=None):
    #pprint("on app teardown_request, showdown sqlite session....")
    db_session.remove()

def connect_db():
    #pprint(os.path.abspath(app.config['DATABASE']))
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            pprint(f.read())
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()


app.add_url_rule('/index/',view_func=views.index)
app.add_url_rule('/ent/',view_func=views.ent)
app.add_url_rule('/',view_func=views.index)
app.add_url_rule('/tes/<test>',view_func=views.testImage)

from picMan import picMan as picMan_blueprint
from rasterviewer import rasterviewer as rasterviewer_blueprint
#注册blueprint到一级路由
#app.register_blueprint(picMan_blueprint)

#注册blueprint 到二级路由
app.register_blueprint(picMan_blueprint,url_prefix="/picman")
app.register_blueprint(rasterviewer_blueprint,url_prefix="/rasterviewer")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
