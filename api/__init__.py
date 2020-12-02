import logging
import  os

from flask import Flask, jsonify, request
from flask_meter import FlaskMeter

from api.controllers.user import user
from api.config import app_config
from api.db import database

flask_meter = FlaskMeter()

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user)

    logger = logging.getLogger()
    logger.setLevel(app_config.LOG_LEVEL)

    app.config.from_object(app_config)

    flask_meter.init_app(app)

    @app.route("/")
    def index():
        payload = {"result": "success"}
        return jsonify(payload)

    return app