# src/models/consejo.py
from src.models import db

class Consejo(db.Model):
    __tablename__ = "consejos"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)
    categoria = db.Column(db.String(100))
    contenido = db.Column(db.Text, nullable=False)
    planta_id = db.Column(db.Integer, db.ForeignKey("plantas.id"), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
