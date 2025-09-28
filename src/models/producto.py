# src/models/producto.py
from src.models import db

class Producto(db.Model):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float, nullable=False, default=0.0)
    categoria = db.Column(db.String(50))
    planta_id = db.Column(db.Integer, db.ForeignKey("plantas.id"), nullable=True)
    insumo_id = db.Column(db.Integer, db.ForeignKey("insumos.id"), nullable=True)
