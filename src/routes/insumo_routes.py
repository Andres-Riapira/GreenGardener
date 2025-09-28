# src/routes/insumo_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.insumo_repository import InsumoRepository
from src.schemas.insumo_schema import InsumoSchema
from flask_jwt_extended import jwt_required

insumo_bp = Blueprint("insumo", __name__)
repo = InsumoRepository()
schema = InsumoSchema()

@insumo_bp.route("/", methods=["GET"])
def list_insumos():
    return jsonify(schema.dump(repo.get_all(), many=True)), 200

@insumo_bp.route("/", methods=["POST"])
@jwt_required()
def create_insumo():
    data = request.get_json() or {}
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    obj = repo.create(**data)
    return schema.dump(obj), 201
