# src/models/usuario.py
from datetime import datetime
from src.models import db

class Usuario(db.Model):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(120), nullable=False)
    correo = db.Column(db.String(150), unique=True, nullable=False)
    contrasena = db.Column(db.String(255), nullable=False)  # hashed
    rol = db.Column(db.String(50), default="cliente", nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    pedidos = db.relationship("Pedido", backref="usuario", lazy="dynamic")
