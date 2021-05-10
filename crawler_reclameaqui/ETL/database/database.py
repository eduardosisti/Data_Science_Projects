from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()

def register_database(flask_app):
    from models.Reclamacoes import Reclamacoes

    with flask_app.app_context():
        db.init_app(flask_app)


def register_migrate(flask_app):
    with flask_app.app_context():
        migrate.init_app(flask_app, db)
