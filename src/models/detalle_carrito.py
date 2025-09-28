# src/models/detalle_carrito.py
from src.models import db

class DetalleCarrito(db.Model):
    __tablename__ = "detalles_carrito"
    id = db.Column(db.Integer, primary_key=True)
    carrito_id = db.Column(db.Integer, db.ForeignKey("carritos.id"), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False, default=1)
    precio_total = db.Column(db.Float, nullable=False, default=0.0)
