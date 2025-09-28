from src.models import db
from src.models.comentario import Comentario

class ComentarioRepository:

    @staticmethod
    def crear(contenido, usuario_id, foro_id):
        comentario = Comentario(contenido=contenido, usuario_id=usuario_id, foro_id=foro_id)
        db.session.add(comentario)
        db.session.commit()
        return comentario

    @staticmethod
    def listar():
        return Comentario.query.all()

    @staticmethod
    def buscar_por_id(comentario_id):
        return Comentario.query.get(comentario_id)

    @staticmethod
    def actualizar(comentario_id, **kwargs):
        comentario = Comentario.query.get(comentario_id)
        if comentario:
            for key, value in kwargs.items():
                setattr(comentario, key, value)
            db.session.commit()
        return comentario

    @staticmethod
    def eliminar(comentario_id):
        comentario = Comentario.query.get(comentario_id)
        if comentario:
            db.session.delete(comentario)
            db.session.commit()
        return comentario

