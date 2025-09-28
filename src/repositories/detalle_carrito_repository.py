from src.models import db
from src.models.detalle_carrito import DetalleCarrito

class DetalleCarritoRepository:

    @staticmethod
    def crear(carrito_id, producto_id, cantidad):
        detalle = DetalleCarrito(carrito_id=carrito_id, producto_id=producto_id, cantidad=cantidad)
        db.session.add(detalle)
        db.session.commit()
        return detalle

    @staticmethod
    def listar():
        return DetalleCarrito.query.all()

    @staticmethod
    def buscar_por_id(detalle_id):
        return DetalleCarrito.query.get(detalle_id)

    @staticmethod
    def actualizar(detalle_id, **kwargs):
        detalle = DetalleCarrito.query.get(detalle_id)
        if detalle:
            for key, value in kwargs.items():
                setattr(detalle, key, value)
            db.session.commit()
        return detalle

    @staticmethod
    def eliminar(detalle_id):
        detalle = DetalleCarrito.query.get(detalle_id)
        if detalle:
            db.session.delete(detalle)
            db.session.commit()
        return detalle

