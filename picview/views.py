import os
from . import picview
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from models import document, category, picfile
from database import db_session
piccategory = category.piccategory
picdocument = document.picdocument

@picview.route("/",methods=["GET","POST"])
@picview.route("/docs/<cateName>/<page>/",methods=["GET","POST"])
def docs(cateName = None, page = None):
    doclist = picdocument.query.all()
    return render_template("/picview/docs.html",docs = doclist)
