# src/models/planta.py
from src.models import db

class Planta(db.Model):
    __tablename__ = "plantas"
    id = db.Column(db.Integer, primary_key=True)
    nombre_comun = db.Column(db.String(120), nullable=False)
    nombre_cientifico = db.Column(db.String(150))
    descripcion = db.Column(db.Text)
    req_luz = db.Column(db.String(100))
    req_agua = db.Column(db.String(100))
    req_suelo = db.Column(db.String(100))
