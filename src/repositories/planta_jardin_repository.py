from src.models import db
from src.models.planta_jardin import PlantaJardin

class PlantaJardinRepository:

    @staticmethod
    def crear(jardin_id, planta_id):
        pj = PlantaJardin(jardin_id=jardin_id, planta_id=planta_id)
        db.session.add(pj)
        db.session.commit()
        return pj

    @staticmethod
    def listar():
        return PlantaJardin.query.all()

    @staticmethod
    def buscar_por_id(pj_id):
        return PlantaJardin.query.get(pj_id)

    @staticmethod
    def actualizar(pj_id, **kwargs):
        pj = PlantaJardin.query.get(pj_id)
        if pj:
            for key, value in kwargs.items():
                setattr(pj, key, value)
            db.session.commit()
        return pj

    @staticmethod
    def eliminar(pj_id):
        pj = PlantaJardin.query.get(pj_id)
        if pj:
            db.session.delete(pj)
            db.session.commit()
        return pj

