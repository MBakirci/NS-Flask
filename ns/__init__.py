# project/__init__.py


from flask import Flask, jsonify, current_app
from flask_cors import CORS

from ns.ns_view import ns_blueprint


def create_app():
    # instantiate the app
    app = Flask(__name__)

    CORS(app)

    # set config
    app.config.from_object('ns.config.DevelopmentConfig')

    # register blueprints
    app.register_blueprint(ns_blueprint)

    @app.route('/')
    def index():
        return current_app.send_static_file('index.html')

    return app
