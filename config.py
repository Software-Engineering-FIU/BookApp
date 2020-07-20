# contains all the configuration variables
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    FLASK_APP = 'bookapp'
    FLASK_CONFIG = 'development'
    RANDOM_SECRET_KEY = os.urandom(32)
    SECRET_KEY = RANDOM_SECRET_KEY

    @staticmethod
    def init_app(app):
        pass

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL',
    'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite'))

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')

class TestingConfig(Config):
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}

