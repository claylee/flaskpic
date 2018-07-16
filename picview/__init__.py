from flask import Blueprint

picview = Blueprint("picview", __name__,template_folder='/templates')
print("picview blueprint name:",__name__)

from picview import views, errors
