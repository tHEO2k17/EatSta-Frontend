from flask import Flask

from app.controller import setup_controller


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    app.register_blueprint(setup_controller.blueprint)

    return app
