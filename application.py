# all the imports
import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from config import Config
from contextlib import closing
import views

	 
app = Flask(__name__)
app.config.from_object(Config)

print(app.config)

def connect_db():
    print(os.path.abspath(app.config['DATABASE']))
    return sqlite3.connect(app.config['DATABASE'])

	
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            print(f.read())
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()
    
    
app.add_url_rule('/index/',view_func=views.index)
    
if __name__ == '__main__':
    app.run()