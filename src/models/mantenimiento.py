# src/models/mantenimiento.py
from datetime import datetime
from src.models import db

class Mantenimiento(db.Model):
    __tablename__ = "mantenimientos"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    fecha_solicitud = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50), default="SOLICITADO")
    descripcion = db.Column(db.Text)
