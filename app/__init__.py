from flask import Flask
from .config import Config
from .db import mysql


def create_app():

    app = Flask(__name__)

    # Load Config
    app.config.from_object(Config)

    # Session Secret Key
    app.secret_key = "zodi_super_secret_key_123"

    # Initialize MySQL
    mysql.init_app(app)

    # Register Routes
    from .routes import main
    app.register_blueprint(main)

    return app