# src/models/pedido.py
from datetime import datetime
from src.models import db

class Pedido(db.Model):
    __tablename__ = "pedidos"
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    fecha_pedido = db.Column(db.DateTime, default=datetime.utcnow)
    estado = db.Column(db.String(50), default="PENDIENTE")
