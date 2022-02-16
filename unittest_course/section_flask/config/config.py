from os import environ, path 
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class BaseConfig:
    TEMPLATES_FOLDER = environ.get('TEMPLATES_FOLDER')
    STATIC_FOLDER = environ.get('STATIC_FOLDER')
    SECRET_KEY = environ.get('SECRET_KEY')

class DevConfig(BaseConfig):
    SERVER_NAME = environ.get('SERVER_NAME')
    TESTING = environ.get('TESTING')
    DEBUG = environ.get('DEBUG')
    FLASK_ENV = environ.get('FLASK_ENV')