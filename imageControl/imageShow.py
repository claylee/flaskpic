import os
import sys
from PIL import Image

class imageShow(object):
    def __init__(self):
        pass

    def getImageThumbnail(path, name, size, itype):
        imagepath =os.path.join(path,name)
        thbPath = str.format("{}/../thumbnail_{}",path,size)
        #print(os.path.abspath(thbPath))
        if not os.path.exists(thbPath):
            os.mkdir(thbPath)

        #print(thbPath)
        #print(name)
        thumbNailName=os.path.join(thbPath,name)
        #print(thumbNailName)
        if os.path.exists(thumbNailName):
            #print("exist:",thumbNailName)
            return thumbNailName
        im=Image.open(imagepath)
        im.thumbnail((int(size),int(size)))
        im.save(thumbNailName,'JPEG')
        return thumbNailName

    def addTransparency(img, factor = 0.7 ):
        img = img.convert('RGBA')
        img_blender = Image.new('RGBA', img.size, (0,0,0,0))
        img = Image.blend(img_blender, img, factor)
        return img

    def ImageMaskLabel(imagePath, labelPath, saveImagePath=None,tunel=0):
        image = Image.open(imagePath)
        label = Image.open(labelPath)
        labelRGB = label.convert("RGBA")
        labelRGB = imageShow.addTransparency(labelRGB,0.5)
        r,g,b,a = labelRGB.split()
        print("tunel:",tunel)
        if tunel == 0:
            tnl = r
        elif tunel == 1:
            tnl = g
        else:
            tnl = b
        print(a)

        image.paste(label, (0,0), mask=a)

        parent_path = os.path.dirname(saveImagePath)
        file_name = os.path.split(saveImagePath)[-1]
        if not os.path.exists(parent_path):
            os.mkdir(parent_path)

        maskPng = "{}/{}_{}".format(parent_path,tunel,file_name)
        ap = "{}/{}_{}".format(parent_path,"a",".png")
        rp = "{}/{}_{}".format(parent_path,tunel,".png")
        gp = "{}/{}_{}".format(parent_path,tunel,".png")
        bp = "{}/{}_{}".format(parent_path,tunel,".png")
        print(maskPng)
        '''
        a.save(ap)
        r.save(rp)
        g.save(gp)
        b.save(bp)
        labelRGB.save(saveImagePath)
        '''
        image.save(maskPng)
        return maskPng
