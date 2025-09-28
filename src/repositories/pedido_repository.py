from src.models import db
from src.models.pedido import Pedido

class PedidoRepository:

    @staticmethod
    def crear(usuario_id, estado="pendiente"):
        pedido = Pedido(usuario_id=usuario_id, estado=estado)
        db.session.add(pedido)
        db.session.commit()
        return pedido

    @staticmethod
    def listar():
        return Pedido.query.all()

    @staticmethod
    def buscar_por_id(pedido_id):
        return Pedido.query.get(pedido_id)

    @staticmethod
    def actualizar(pedido_id, **kwargs):
        pedido = Pedido.query.get(pedido_id)
        if pedido:
            for key, value in kwargs.items():
                setattr(pedido, key, value)
            db.session.commit()
        return pedido

    @staticmethod
    def eliminar(pedido_id):
        pedido = Pedido.query.get(pedido_id)
        if pedido:
            db.session.delete(pedido)
            db.session.commit()
        return pedido

