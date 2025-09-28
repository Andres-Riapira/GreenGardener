# src/models/diseno.py
from datetime import datetime
from src.models import db

class Diseno(db.Model):
    __tablename__ = "disenos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    jardin_id = db.Column(db.Integer, db.ForeignKey("jardines_virtuales.id"), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
