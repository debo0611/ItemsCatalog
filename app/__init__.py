import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_type):
    """
    create app
    """
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)
    bootstrap.init_app(app)

    from app.catalog import catalog
    app.register_blueprint(catalog)

    from app.auth import auth
    app.register_blueprint(auth)

    from app.api import api
    app.register_blueprint(api)

    return app
