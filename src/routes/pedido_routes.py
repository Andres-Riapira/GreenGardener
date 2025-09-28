from flask import Blueprint, jsonify, request

# src/routes/pedido_routes.py
from flask import Blueprint, request, jsonify
from src.models.pedido import Pedido
from src.models.detalle_pedido import DetallePedido
from src.models import db
from flask_jwt_extended import jwt_required, get_jwt_identity

pedido_bp = Blueprint("pedido", __name__)

@pedido_bp.route("/", methods=["POST"])
@jwt_required()
def create_pedido():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    try:
        pedido = Pedido(usuario_id=user_id)
        db.session.add(pedido)
        db.session.flush()
        detalles = data.get("detalles", [])
        total = 0
        for d in detalles:
            dp = DetallePedido(pedido_id=pedido.id, producto_id=d["producto_id"], cantidad=d["cantidad"], precio_total=d.get("precio_total", 0))
            db.session.add(dp)
            total += dp.precio_total
        pedido.estado = "CONFIRMADO"
        db.session.commit()
        return jsonify({"id": pedido.id, "total": total}), 201
    except Exception:
        db.session.rollback()
        raise
