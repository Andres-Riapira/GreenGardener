from src.models import db
from src.models.producto import Producto

class ProductoRepository:

    @staticmethod
    def crear(nombre, precio, planta_id=None):
        producto = Producto(nombre=nombre, precio=precio, planta_id=planta_id)
        db.session.add(producto)
        db.session.commit()
        return producto

    @staticmethod
    def listar():
        return Producto.query.all()

    @staticmethod
    def buscar_por_id(producto_id):
        return Producto.query.get(producto_id)

    @staticmethod
    def actualizar(producto_id, **kwargs):
        producto = Producto.query.get(producto_id)
        if producto:
            for key, value in kwargs.items():
                setattr(producto, key, value)
            db.session.commit()
        return producto

    @staticmethod
    def eliminar(producto_id):
        producto = Producto.query.get(producto_id)
        if producto:
            db.session.delete(producto)
            db.session.commit()
        return producto

