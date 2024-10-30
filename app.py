import os
from flask import Flask

from config import SECRET_KEY
from routes import routes


def create_app(test_config=None):
    # creating an app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
    )

    # registering blueprints
    app.register_blueprint(routes)

    if test_config is None:
        # load config file
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load test config file
        app.config.from_mapping(test_config)

    # ensure that instance path is exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
