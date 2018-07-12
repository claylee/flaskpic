import os
import sys
from PIL import Image

class imageShow(object):
    def getImageThumbnail(path, name, size, itype):
        name=os.path.join(path,name)
        thbPath = str.format("/../thumbnail_{}",size)
        if not os.path.exists(thbPath):
            os.mkdir(thbPath)

        thumbNailName=os.path.join(thbPath,name)
        if os.path.exists(thumbNailName):
            #print("exist:",thumbNailName)
            return thumbNailName
        im=Image.open(name)
        im.thumbnail((int(size),int(size)))
        im.save(thumbNailName,'JPEG')
        return thumbNailName
