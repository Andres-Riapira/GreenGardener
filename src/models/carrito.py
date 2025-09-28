# src/models/carrito.py
from datetime import datetime
from src.models import db

class Carrito(db.Model):
    __tablename__ = "carritos"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
