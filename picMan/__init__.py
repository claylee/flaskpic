from flask import Blueprint

picMan = Blueprint("picMan", __name__,template_folder='/templates')
print("picman blueprint name:",__name__)

from picMan import views, errors


#from ..models import Permission
