from src.models import db
from src.models.usuario import Usuario

class UsuarioRepository:

    @staticmethod
    def crear(nombre, correo, contraseña, rol="usuario"):
        usuario = Usuario(nombre=nombre, correo=correo, contraseña=contraseña, rol=rol)
        db.session.add(usuario)
        db.session.commit()
        return usuario

    @staticmethod
    def listar():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_id(usuario_id):
        return Usuario.query.get(usuario_id)

    @staticmethod
    def actualizar(usuario_id, **kwargs):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            for key, value in kwargs.items():
                setattr(usuario, key, value)
            db.session.commit()
        return usuario

    @staticmethod
    def eliminar(usuario_id):
        usuario = Usuario.query.get(usuario_id)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
        return usuario

