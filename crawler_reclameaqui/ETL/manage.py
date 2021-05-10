from parsers.main import insert_carga
from flask.cli import AppGroup
from flask import Flask
from database.database import register_database, register_migrate
import os


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_SERVICE_NAME')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    # app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://postgres:yourpasswordhere12345@localhost:54320/reclameaqui"

    register_database(app)
    register_migrate(app)
    app.app_context().push()

    insert_carga()

    return app

flask_app = create_app()