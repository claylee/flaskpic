import os
from . import rasterviewer
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, Response,send_file,make_response
from models import document, category, picfile
from database import db_session
from imageControl import imageShow #getImageThumbnail
from application import app
from rasterConfig import RasterRoots
from . import baseController

import json
imgShow = imageShow.imageShow
getImageThumbnail = imageShow.imageShow.getImageThumbnail
piccategory = category.piccategory
picdocument = document.picdocument

class RasterViews(baseController.base):
    """docstring for RasterViews."""
    def __init__(self):
        super(RasterViews, self).__init__()
        #self.arg = arg

    @rasterviewer.route("/",methods=["GET","POST"])
    @rasterviewer.route("/index/",methods=["GET","POST"])
    def index():
        errors = RasterViews.GetErrorList()
        return render_template("rasterviewer/index.html",\
        rasterNames=RasterViews.getRasterNames(),\
        errorList=errors)

    @rasterviewer.route("/imagepair/<name>/<size>",methods=["GET","POST"])
    def imagePair(name=None,size=0):
        return render_template("rasterviewer/imagePair.html",name=name,size=size)

    @rasterviewer.route("/pickerror/<name>/<size>",methods=["GET","POST"])
    def pickerror(name=None,size=0):
        errorNames = RasterViews.GetErrorList()
        errors = False
        if name in errorNames:
            errors = True
        print("error:",errors)
        return render_template("rasterviewer/pickLabelError.html",name=name,size=size,errors=errors)

    @rasterviewer.route("/tipError/<name>",methods=["GET","POST"])
    def tipError(name=None):
        errorNames = GetErrorList()
        if name not in errorNames:
            errorNames.append(name)
        print(errorNames)
        SaveErrorList(errorNames)
        return "True"

    @rasterviewer.route("/untipError/<name>",methods=["GET","POST"])
    def untipError(name=None):
        errorNames = GetErrorList()
        print(name)
        if name in errorNames:
            errorNames.remove(name)
        SaveErrorList(errorNames)
        print(errorNames)
        return "True"

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

    def GetErrorList():
        rasterRoot="D:/ImageSplite/tiffdata/LabelRnd"
        imageNamesError = "error"
        imageNamesError  = '{}/{}.txt'.format(rasterRoot, imageNamesError)

        errorNames = None
        with open(imageNamesError, 'r' ) as fp:
            errorNames = fp.read().splitlines()
        #errorNames = open(imageNamesError, 'r').read().splitlines()
        return errorNames

    def SaveErrorList(errorNames):
        rasterRoot="D:/ImageSplite/tiffdata/LabelRnd"
        imageNamesError = "error"
        imageNamesError  = '{}/{}.txt'.format(rasterRoot, imageNamesError)
        with open(imageNamesError, 'w+' ) as fp:
            fp.write("\n".join(errorNames))


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
        #rasterRoot="D:/ImageSplite/tiffdata/LabelRnd"
        rasterRoot = RasterViews.GetCurRasterPath()
        print(rasterRoot)
        imageNamesTrain="train"
        imageNamesVal="val"


        imageNamesTrain  = '{}/{}.txt'.format(rasterRoot, imageNamesTrain)
        rasterNames = open(imageNamesTrain, 'r').read().splitlines()

        imageNamesVal  = '{}/{}.txt'.format(rasterRoot, imageNamesVal)
        rasterNames = rasterNames + (open(imageNamesVal, 'r').read().splitlines())
        return rasterNames

    @rasterviewer.route('/rasterDb/')
    def rasterdb():
        #dbList = app.config["RASTERDB"]
        rasterList = RasterRoots.loadRasterList()
        return render_template("/rasterviewer/category.html",cateList = rasterList)

    @rasterviewer.route('/thumbCombin/')
    @rasterviewer.route('/thumbCombin/<rtype>')
    def rasterThumbCombin(rtype="Image"):
        rasterRoot= RasterViews.GetCurRasterPath()#"D:/ImageSplite/tiffdata/LabelRnd/"
        print(rasterRoot)
        imageNames = RasterViews.getRasterNames()
        imagePath = imgShow.ImageCombinThumb(rasterRoot,rtype,imageNames)
        image = open(imagePath, "rb").read()
        response = make_response(image)
        response.headers['Content-Type'] = 'image/jpeg'
        return response

    @rasterviewer.route('/setrasterset/<dbname>')
    def setrasterset(dbname=""):
        session["curRasterSet"] = dbname
        return redirect(url_for('rasterviewer.index'))
