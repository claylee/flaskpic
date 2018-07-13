import os
from . import rasterviewer
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, Response,send_file,make_response
from models import document, category, picfile
from database import db_session
from imageControl import imageShow #getImageThumbnail
imgShow = imageShow.imageShow
getImageThumbnail = imageShow.imageShow.getImageThumbnail
piccategory = category.piccategory
picdocument = document.picdocument

@rasterviewer.route("/",methods=["GET","POST"])
@rasterviewer.route("/index/",methods=["GET","POST"])
def index():
    return render_template("rasterviewer/index.html",rasterNames=getRasterNames())

@rasterviewer.route("/imagepair/<name>/<size>",methods=["GET","POST"])
def imagePair(name=None,size=0):
    return render_template("rasterviewer/imagePair.html",name=name,size=size)

@rasterviewer.route("/imageMask/<name>/<tunel>",methods=["GET","POST"])
def imageMask(name=None,tunel=0):
    rasterRoot="D:/ImageSplite/tiffdata/LabelRnd"
    imagePath = "{}/{}/{}.jpg".format(rasterRoot,"Image",name)
    labelPath = "{}/{}/Label_{}.png".format(rasterRoot,"Label",name)
    savePath = "{}/{}/{}.png".format(rasterRoot,"Mask",name)
    maskPngPath = imgShow.ImageMaskLabel(imagePath,labelPath,savePath,tunel)

    image = open(maskPngPath, "rb").read()
    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpeg'
    return response

@rasterviewer.route("/readRasterImage/<name>/<rtype>",methods=["GET","POST"])
def readRasterImage(name=None,rtype="Image"):
    rasterRoot="D:/ImageSplite/tiffdata/LabelRnd"
    if rtype == "Image":
        name = "{}.jpg".format(name)
    else:
        name = "Label_{}.png".format(name)

    image = open("{}/{}/{}".format(rasterRoot,rtype,name), "rb").read()

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
