import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import config as Config
from flask_bootstrap import Bootstrap

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'user.signup'

def create_app(config):
    app = Flask(__name__)
    config_name = config

    if not isinstance(config, str):
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app.config.from_object(Config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Config[config_name].init_app(app)

    db.init_app(app)
    login_manager.init_app(app)

    Bootstrap(app)
    # blueprint + routes
    from .user import user as user
    app.register_blueprint(user, url_prefix='/user')

    return app




