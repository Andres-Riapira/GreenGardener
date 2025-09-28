from src.models import db
from src.models.consejo import Consejo

class ConsejoRepository:

    @staticmethod
    def crear(titulo, contenido, usuario_id):
        consejo = Consejo(titulo=titulo, contenido=contenido, usuario_id=usuario_id)
        db.session.add(consejo)
        db.session.commit()
        return consejo

    @staticmethod
    def listar():
        return Consejo.query.all()

    @staticmethod
    def buscar_por_id(consejo_id):
        return Consejo.query.get(consejo_id)

    @staticmethod
    def actualizar(consejo_id, **kwargs):
        consejo = Consejo.query.get(consejo_id)
        if consejo:
            for key, value in kwargs.items():
                setattr(consejo, key, value)
            db.session.commit()
        return consejo

    @staticmethod
    def eliminar(consejo_id):
        consejo = Consejo.query.get(consejo_id)
        if consejo:
            db.session.delete(consejo)
            db.session.commit()
        return consejo

