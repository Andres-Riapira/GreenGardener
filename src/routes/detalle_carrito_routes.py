from flask import Blueprint, jsonify, request

# src/routes/detalle_carrito_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.detalle_carrito_repository import DetalleCarritoRepository
from src.schemas.detalle_carrito_schema import DetalleCarritoSchema
from flask_jwt_extended import jwt_required

detalle_carrito_bp = Blueprint("detalle_carrito", __name__)
repo = DetalleCarritoRepository()
schema = DetalleCarritoSchema()

@detalle_carrito_bp.route("/", methods=["POST"])
@jwt_required()
def add_detalle():
    data = request.get_json() or {}
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    item = repo.create(**data)
    return schema.dump(item), 201

@detalle_carrito_bp.route("/", methods=["GET"])
@jwt_required()
def list_detalles():
    items = repo.get_all()
    return jsonify(schema.dump(items, many=True)), 200
