# src/models/detalle_pedido.py
from src.models import db

class DetallePedido(db.Model):
    __tablename__ = "detalles_pedido"
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey("pedidos.id"), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    precio_total = db.Column(db.Float, nullable=False)
