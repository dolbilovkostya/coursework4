class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PWD_SALT = b'Very secret'
    PWD_ITERATIONS = 100_000
    JWT_ALGO = 'HS256'

