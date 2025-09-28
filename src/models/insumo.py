# src/models/insumo.py
from src.models import db

class Insumo(db.Model):
    __tablename__ = "insumos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    descripcion = db.Column(db.Text)
    precio = db.Column(db.Float, default=0.0)
