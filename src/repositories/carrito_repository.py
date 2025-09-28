from src.models import db
from src.models.carrito import Carrito

class CarritoRepository:

    @staticmethod
    def crear(usuario_id):
        carrito = Carrito(usuario_id=usuario_id)
        db.session.add(carrito)
        db.session.commit()
        return carrito

    @staticmethod
    def listar():
        return Carrito.query.all()

    @staticmethod
    def buscar_por_id(carrito_id):
        return Carrito.query.get(carrito_id)

    @staticmethod
    def actualizar(carrito_id, **kwargs):
        carrito = Carrito.query.get(carrito_id)
        if carrito:
            for key, value in kwargs.items():
                setattr(carrito, key, value)
            db.session.commit()
        return carrito

    @staticmethod
    def eliminar(carrito_id):
        carrito = Carrito.query.get(carrito_id)
        if carrito:
            db.session.delete(carrito)
            db.session.commit()
        return carrito

