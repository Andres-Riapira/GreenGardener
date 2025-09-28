from src.models import db
from src.models.foro import Foro

class ForoRepository:

    @staticmethod
    def crear(titulo, descripcion, usuario_id):
        foro = Foro(titulo=titulo, descripcion=descripcion, usuario_id=usuario_id)
        db.session.add(foro)
        db.session.commit()
        return foro

    @staticmethod
    def listar():
        return Foro.query.all()

    @staticmethod
    def buscar_por_id(foro_id):
        return Foro.query.get(foro_id)

    @staticmethod
    def actualizar(foro_id, **kwargs):
        foro = Foro.query.get(foro_id)
        if foro:
            for key, value in kwargs.items():
                setattr(foro, key, value)
            db.session.commit()
        return foro

    @staticmethod
    def eliminar(foro_id):
        foro = Foro.query.get(foro_id)
        if foro:
            db.session.delete(foro)
            db.session.commit()
        return foro

