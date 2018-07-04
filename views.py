from flask import Flask
from flask import render_template,current_app


def index(name=None):
    return render_template('index.html', name=name)
    

def ent(name=None):
    return render_template('entities.html', name=name)