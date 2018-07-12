from flask import Blueprint

rasterviewer = Blueprint("rasterviewer", __name__,template_folder='/templates')
print("rasterviewer blueprint name:",__name__)

from rasterviewer import views
