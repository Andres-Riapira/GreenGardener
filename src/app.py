"""
Fábrica de la aplicación Flask.
Registra blueprints y prepara extensiones.
"""
from flask import Flask
from src.config import Config
from src.models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)

    # Registrar blueprints (rutas)
    from src.routes.usuario_routes import usuario_bp
    from src.routes.planta_routes import planta_bp
    from src.routes.insumo_routes import insumo_bp
    from src.routes.producto_routes import producto_bp
    from src.routes.carrito_routes import carrito_bp
    from src.routes.detalle_carrito_routes import detalle_carrito_bp
    from src.routes.pedido_routes import pedido_bp
    from src.routes.detalle_pedido_routes import detalle_pedido_bp
    from src.routes.mantenimiento_routes import mantenimiento_bp
    from src.routes.foro_routes import foro_bp
    from src.routes.comentario_routes import comentario_bp
    from src.routes.consejo_routes import consejo_bp
    from src.routes.jardin_virtual_routes import jardin_virtual_bp
    from src.routes.planta_jardin_routes import planta_jardin_bp
    from src.routes.diseno_routes import diseno_bp

    app.register_blueprint(usuario_bp, url_prefix="/usuarios")
    app.register_blueprint(planta_bp, url_prefix="/plantas")
    app.register_blueprint(insumo_bp, url_prefix="/insumos")
    app.register_blueprint(producto_bp, url_prefix="/productos")
    app.register_blueprint(carrito_bp, url_prefix="/carritos")
    app.register_blueprint(detalle_carrito_bp, url_prefix="/detalles_carrito")
    app.register_blueprint(pedido_bp, url_prefix="/pedidos")
    app.register_blueprint(detalle_pedido_bp, url_prefix="/detalles_pedido")
    app.register_blueprint(mantenimiento_bp, url_prefix="/mantenimientos")
    app.register_blueprint(foro_bp, url_prefix="/foros")
    app.register_blueprint(comentario_bp, url_prefix="/comentarios")
    app.register_blueprint(consejo_bp, url_prefix="/consejos")
    app.register_blueprint(jardin_virtual_bp, url_prefix="/jardines")
    app.register_blueprint(planta_jardin_bp, url_prefix="/plantas_jardin")
    app.register_blueprint(diseno_bp, url_prefix="/disenos")

    @app.route("/")
    def home():
        return "🌱 GreenGardener API - Running"

    return app

if __name__ == "__main__":
    create_app().run(debug=True)
