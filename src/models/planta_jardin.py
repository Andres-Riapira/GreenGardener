# src/models/planta_jardin.py
from src.models import db

class PlantaJardin(db.Model):
    __tablename__ = "plantas_jardin"
    id = db.Column(db.Integer, primary_key=True)
    jardin_id = db.Column(db.Integer, db.ForeignKey("jardines_virtuales.id"), nullable=False)
    planta_id = db.Column(db.Integer, db.ForeignKey("plantas.id"), nullable=False)
    pos_x = db.Column(db.Integer, default=0)
    pos_y = db.Column(db.Integer, default=0)
    fecha_plantacion = db.Column(db.Date)
