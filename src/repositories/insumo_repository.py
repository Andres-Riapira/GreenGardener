from src.models import db
from src.models.insumo import Insumo

class InsumoRepository:

    @staticmethod
    def crear(nombre, descripcion, stock=0):
        insumo = Insumo(nombre=nombre, descripcion=descripcion, stock=stock)
        db.session.add(insumo)
        db.session.commit()
        return insumo

    @staticmethod
    def listar():
        return Insumo.query.all()

    @staticmethod
    def buscar_por_id(insumo_id):
        return Insumo.query.get(insumo_id)

    @staticmethod
    def actualizar(insumo_id, **kwargs):
        insumo = Insumo.query.get(insumo_id)
        if insumo:
            for key, value in kwargs.items():
                setattr(insumo, key, value)
            db.session.commit()
        return insumo

    @staticmethod
    def eliminar(insumo_id):
        insumo = Insumo.query.get(insumo_id)
        if insumo:
            db.session.delete(insumo)
            db.session.commit()
        return insumo

