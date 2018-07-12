import os
from . import rasterviewer
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, Response,send_file,make_response
from models import document, category, picfile
from database import db_session
from imageControl import imageShow #getImageThumbnail
getImageThumbnail = imageShow.imageShow.getImageThumbnail
piccategory = category.piccategory
picdocument = document.picdocument

@rasterviewer.route("/",methods=["GET","POST"])
def index():
    return render_template("rasterviewer/index.html",rasterNames=getRasterNames())


@rasterviewer.route("/readRasterImage/<name>/<rtype>",methods=["GET","POST"])
def readRasterImage(name=None,rtype="image"):
    rasterRoot="D:/ImageSplite/tiffdata/LabelRnd"
    image = open("{}/Image/{}.jpg".format(rasterRoot,name), "rb").read()

    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpeg'
    return response

@rasterviewer.route("/readThumb/<name>/<rtype>/<size>",methods=["GET","POST"])
def readThumb(name=None,rtype="Image",size=64):
    rasterRoot="D:/ImageSplite/tiffdata/LabelRnd"
    if rtype == "Image":
        name = name + ".jpg"
    else:
        name = "Label_" + name + ".png"
    thbPath = getImageThumbnail(rasterRoot+"/"+rtype,name,size,"jpeg")
    image = open(thbPath, "rb").read()

    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpeg'
    return response

@rasterviewer.route("/getRasterNames/",methods=["GET","POST"])
def getRasterNames():
    rasterRoot="D:/ImageSplite/tiffdata/LabelRnd"
    imageNamesTrain="train"
    imageNamesVal="val"


    imageNamesTrain  = '{}/{}.txt'.format(rasterRoot, imageNamesTrain)
    rasterNames = open(imageNamesTrain, 'r').read().splitlines()

    imageNamesVal  = '{}/{}.txt'.format(rasterRoot, imageNamesVal)
    rasterNames = rasterNames + (open(imageNamesVal, 'r').read().splitlines())
    return rasterNames
