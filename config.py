class Config(object):
    SECRET_KEY = 'my_UNAL_key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
