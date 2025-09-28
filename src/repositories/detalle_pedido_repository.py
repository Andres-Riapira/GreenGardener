from src.models import db
from src.models.detalle_pedido import DetallePedido

class DetallePedidoRepository:

    @staticmethod
    def crear(pedido_id, producto_id, cantidad):
        detalle = DetallePedido(pedido_id=pedido_id, producto_id=producto_id, cantidad=cantidad)
        db.session.add(detalle)
        db.session.commit()
        return detalle

    @staticmethod
    def listar():
        return DetallePedido.query.all()

    @staticmethod
    def buscar_por_id(detalle_id):
        return DetallePedido.query.get(detalle_id)

    @staticmethod
    def actualizar(detalle_id, **kwargs):
        detalle = DetallePedido.query.get(detalle_id)
        if detalle:
            for key, value in kwargs.items():
                setattr(detalle, key, value)
            db.session.commit()
        return detalle

    @staticmethod
    def eliminar(detalle_id):
        detalle = DetallePedido.query.get(detalle_id)
        if detalle:
            db.session.delete(detalle)
            db.session.commit()
        return detalle

