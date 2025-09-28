# src/repositories/diseno_repository.py

from src.models.diseno import Diseno
from src.models import db

class DisenoRepository:
    """Repositorio para manejar operaciones de la entidad Diseno"""

    @staticmethod
    def get_all():
        return Diseno.query.all()

    @staticmethod
    def get_by_id(diseno_id):
        return Diseno.query.get(diseno_id)

    @staticmethod
    def create(data):
        diseno = Diseno(**data)
        db.session.add(diseno)
        db.session.commit()
        return diseno

    @staticmethod
    def update(diseno_id, data):
        diseno = Diseno.query.get(diseno_id)
        if diseno:
            for key, value in data.items():
                setattr(diseno, key, value)
            db.session.commit()
        return diseno

    @staticmethod
    def delete(diseno_id):
        diseno = Diseno.query.get(diseno_id)
        if diseno:
            db.session.delete(diseno)
            db.session.commit()
        return diseno
