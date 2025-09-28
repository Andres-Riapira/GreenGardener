# src/models/jardin_virtual.py
from datetime import datetime
from src.models import db

class JardinVirtual(db.Model):
    __tablename__ = "jardines_virtuales"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
