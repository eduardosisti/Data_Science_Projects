from database.database import db
from models.base import BaseModel
from sqlalchemy.dialects.postgresql import JSON


class Reclamacoes(db.Model, BaseModel):
    __tablename__ = 'reclamacoes'

    titulo = db.Column(db.String(300), nullable=True)
    descricao = db.Column(db.String(5000), nullable=True)
    cidade = db.Column(db.String(100), nullable=True)
    estado = db.Column(db.String(2), nullable=True)
    id = db.Column(db.Integer, nullable=True)
    data = db.Column(db.Date, nullable=True)
    hora = db.Column(db.Time, nullable=True)
    link = db.Column(db.String(200), nullable=False, primary_key=True)
    dominio = db.Column(db.String(50), nullable=True)
    titulo_json = db.Column(db.JSON, nullable=True)
    descricao_json = db.Column(db.JSON, nullable=True)
    classes_titulo = db.Column(db.JSON, nullable=True)
    classes_descricao = db.Column(db.JSON, nullable=True)
    classes = db.Column(db.JSON, nullable=True)