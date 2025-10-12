from flask import Flask
from flask_cors import CORS
from .config import Config
from .db import db
from .routes.entries import entries_bp
from .routes.ideas import ideas_bp
from .routes.categories import categories_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Initialize DB
    db.init_app(app)

    # Import models after db.init_app
    from .models import Entry, Image, Category, DateIdea, Link

    # Register blueprints
    app.register_blueprint(entries_bp, url_prefix="/api")
    app.register_blueprint(ideas_bp, url_prefix="/api")
    app.register_blueprint(categories_bp, url_prefix="/api")

    return app
