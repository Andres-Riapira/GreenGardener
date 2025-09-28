from src.models import db
from src.models.mantenimiento import Mantenimiento

class MantenimientoRepository:

    @staticmethod
    def crear(usuario_id, descripcion, fecha):
        mantenimiento = Mantenimiento(usuario_id=usuario_id, descripcion=descripcion, fecha=fecha)
        db.session.add(mantenimiento)
        db.session.commit()
        return mantenimiento

    @staticmethod
    def listar():
        return Mantenimiento.query.all()

    @staticmethod
    def buscar_por_id(mantenimiento_id):
        return Mantenimiento.query.get(mantenimiento_id)

    @staticmethod
    def actualizar(mantenimiento_id, **kwargs):
        mantenimiento = Mantenimiento.query.get(mantenimiento_id)
        if mantenimiento:
            for key, value in kwargs.items():
                setattr(mantenimiento, key, value)
            db.session.commit()
        return mantenimiento

    @staticmethod
    def eliminar(mantenimiento_id):
        mantenimiento = Mantenimiento.query.get(mantenimiento_id)
        if mantenimiento:
            db.session.delete(mantenimiento)
            db.session.commit()
        return mantenimiento

