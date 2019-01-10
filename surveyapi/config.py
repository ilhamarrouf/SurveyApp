class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = 'mysupersecretkey'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///survey.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
