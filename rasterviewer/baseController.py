from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, Response,send_file,make_response
from rasterConfig import RasterRoots

class base(object):
    """docstring for baseController."""
    def __init__(self):
        super(base, self).__init__()
        #self.arg = arg

    def GetCurRasterset():
        rasterSet = []
        if "curRasterSet" in session:
            rasterSet = RasterRoots.loadRaster(session["curRasterSet"])
        else:
            rasterSet = None


    def GetCurRasterPath():
        rasterSet = []
        if "curRasterSet" in session:
            rasterSet = RasterRoots.loadRaster(session["curRasterSet"])
            return rasterSet["path"]
        else:
            rasterSet = RasterRoots.loadRasterList()
            print('rasterSet[0]["path"]')
            print(rasterSet[0]["path"])
            return rasterSet[0]["path"]
