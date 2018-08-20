import json
import os

def loadRasterList():
    rasterList = {}
    with open("rasterConfig/RasterRoots.json", 'r', encoding='utf-8') as f:
        print(f)
        rasterList = json.loads(f.read())
    return rasterList

def loadRaster(name):
    rasterList = loadRasterList()
    for r in rasterList:
        if r["name"] == name:
            return r
    return None
