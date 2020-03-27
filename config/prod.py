import os


DEBUG = False
SECRET_KEY = '381blackwell'
SQLALCHEMY_DATABASE_URI = os.environ['postgresql://postgres:381blackwell@localhost/catalog_db']
SQLALCHEMY_TRACK_MODIFICATIONS = False