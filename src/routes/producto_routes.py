# src/routes/producto_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.producto_repository import ProductoRepository
from src.schemas.producto_schema import ProductoSchema
from flask_jwt_extended import jwt_required

producto_bp = Blueprint("producto", __name__)
repo = ProductoRepository()
schema = ProductoSchema()

@producto_bp.route("/", methods=["GET"])
def list_productos():
    return jsonify(schema.dump(repo.get_all(), many=True)), 200

@producto_bp.route("/", methods=["POST"])
@jwt_required()
def create_producto():
    data = request.get_json() or {}
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    p = repo.create(**data)
    return schema.dump(p), 201
