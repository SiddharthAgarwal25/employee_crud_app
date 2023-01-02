from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class create_app:
    def create_app(self):
        app = Flask(__name__)
        db.init_app(app)
        return app

