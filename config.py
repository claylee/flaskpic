# configuration

class Config(object):
	DATABASE = 'tmp/flaskr.db'
	DEBUG = True
	SECRET_KEY = 'development key'
	USERNAME = 'admin'
	PASSWORD = 'default'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/flaskr.db'
	RASTERDB = [{'path':'D:/ImageSplite/tiffdata/LabelRnd','name':'高淳土地利用影像'},\
	{'path':'','name':''}]
