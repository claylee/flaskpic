import os
from . import picview
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from models import document, category, picfile
from database import db_session
piccategory = category.piccategory
picdocument = document.picdocument
picfile = picfile.picfile

@picview.route("/",methods=["GET","POST"])
@picview.route("/docs/<cateName>/<page>/",methods=["GET","POST"])
def docs(cateName = None, page = 0, pagesize=20):
    page = int(page)
    if(page == None or page == 0):
        page = 1
    paginations = picdocument.query.filter().paginate(page, pagesize,error_out=False)
    doclist = paginations.items
    pages = paginations.pages
    total = paginations.total

    for l in doclist:
        #print(l.title)
        l.cover = docCover(l.title)

    return render_template("/picview/docs.html",docs = doclist, pages = pages)

@picview.route("/files/",methods=["GET","POST"])
@picview.route("/files/<docName>/",methods=["GET","POST"])
def files(docName = None, page = 0, pagesize = 5):
    page = int(page)
    if(page == None or page == 0):
        page = 1

    filelist = picfile.query.filter(picfile.pictitle == docName).all()
    return render_template("/picview/files.html",files = filelist)

@picview.route("/docCover/<docname>/",methods=["GET","POST"])
def docCover(docname = None):
    pics = picfile.query.filter(picfile.pictitle == docname).all()

    return pics[len(pics)-1].picurl
