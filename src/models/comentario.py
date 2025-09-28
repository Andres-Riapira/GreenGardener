# src/models/comentario.py
from datetime import datetime
from src.models import db

class Comentario(db.Model):
    __tablename__ = "comentarios"
    id = db.Column(db.Integer, primary_key=True)
    foro_id = db.Column(db.Integer, db.ForeignKey("foros.id"), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_comentario = db.Column(db.DateTime, default=datetime.utcnow)
