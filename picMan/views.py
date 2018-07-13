import os
from . import picMan
from .picTree import picTree
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from models import document, category, picfile
from database import db_session
piccategory = category.piccategory
picdocument = document.picdocument

@picMan.route("/",methods=["GET","POST"])
@picMan.route("/index/",methods=["GET","POST"])
def index():
    pictree = picTree()
    return render_template("picMan/index.html",cate=pictree.GetCategory())

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
    return render_template("picMan/pictree.html")

@picMan.route("/documentList",methods=["GET"])
def documentList(docid=-1):
    doc = picdocument()
    return render_template("picMan/docList.html", \
        docList= doc.query.filter(picdocument.pdocid == docid))
