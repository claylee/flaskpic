import os
from . import picMan
from .picTree import picTree
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

@picMan.route("/",methods=["GET","POST"])
def index():
    pictree = picTree()
    return render_template("picman/index.html",cate=pictree.GetCategory())

@picMan.route("/AddCate",methods=["GET","POST"])
def addCategory(title=None,name=None,picpath=None):
    form = request.form
    print(title,name,picpath)
    print(form)
    if("title" in form):
        pictree = picTree()
        print(form["title"],form["text"],form["picpath"])
        pictree.AddCategory(form["title"],form["text"],form["picpath"])
        return redirect(url_for("picMan.index"))
    return render_template("picman/pictree.html")
