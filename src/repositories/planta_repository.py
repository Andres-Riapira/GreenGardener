from src.models import db
from src.models.planta import Planta

class PlantaRepository:

    @staticmethod
    def crear(nombre, descripcion, precio):
        planta = Planta(nombre=nombre, descripcion=descripcion, precio=precio)
        db.session.add(planta)
        db.session.commit()
        return planta

    @staticmethod
    def listar():
        return Planta.query.all()

    @staticmethod
    def buscar_por_id(planta_id):
        return Planta.query.get(planta_id)

    @staticmethod
    def actualizar(planta_id, **kwargs):
        planta = Planta.query.get(planta_id)
        if planta:
            for key, value in kwargs.items():
                setattr(planta, key, value)
            db.session.commit()
        return planta

    @staticmethod
    def eliminar(planta_id):
        planta = Planta.query.get(planta_id)
        if planta:
            db.session.delete(planta)
            db.session.commit()
        return planta

