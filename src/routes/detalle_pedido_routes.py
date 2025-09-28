from flask import Blueprint, jsonify, request

# src/routes/detalle_pedido_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.detalle_pedido_repository import DetallePedidoRepository
from src.schemas.detalle_pedido_schema import DetallePedidoSchema
from flask_jwt_extended import jwt_required

detalle_pedido_bp = Blueprint("detalle_pedido", __name__)
repo = DetallePedidoRepository()
schema = DetallePedidoSchema()

@detalle_pedido_bp.route("/", methods=["POST"])
@jwt_required()
def create_detalle_pedido():
    data = request.get_json() or {}
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    dp = repo.create(**data)
    return schema.dump(dp), 201

@detalle_pedido_bp.route("/", methods=["GET"])
@jwt_required()
def list_detalles_pedido():
    items = repo.get_all()
    return jsonify(schema.dump(items, many=True)), 200
