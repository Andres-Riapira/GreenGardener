from src.models import db
from src.models.jardin_virtual import JardinVirtual

class JardinVirtualRepository:

    @staticmethod
    def crear(usuario_id, nombre):
        jardin = JardinVirtual(usuario_id=usuario_id, nombre=nombre)
        db.session.add(jardin)
        db.session.commit()
        return jardin

    @staticmethod
    def listar():
        return JardinVirtual.query.all()

    @staticmethod
    def buscar_por_id(jardin_id):
        return JardinVirtual.query.get(jardin_id)

    @staticmethod
    def actualizar(jardin_id, **kwargs):
        jardin = JardinVirtual.query.get(jardin_id)
        if jardin:
            for key, value in kwargs.items():
                setattr(jardin, key, value)
            db.session.commit()
        return jardin

    @staticmethod
    def eliminar(jardin_id):
        jardin = JardinVirtual.query.get(jardin_id)
        if jardin:
            db.session.delete(jardin)
            db.session.commit()
        return jardin

