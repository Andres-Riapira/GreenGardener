from flask import Blueprint, jsonify, request

mantenimiento_bp = Blueprint("mantenimiento", __name__)

# Datos de ejemplo de mantenimientos
mantenimientos = [
    {"id": 1, "usuario_id": 1, "planta_id": 2, "descripcion": "Riego semanal", "fecha": "2024-09-01"}, ]
# src/routes/mantenimiento_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.mantenimiento_repository import MantenimientoRepository
from src.schemas.mantenimiento_schema import MantenimientoSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

mantenimiento_bp = Blueprint("mantenimiento", __name__)
repo = MantenimientoRepository()
schema = MantenimientoSchema()

@mantenimiento_bp.route("/", methods=["POST"])
@jwt_required()
def solicitar():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    data["usuario_id"] = user_id
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    m = repo.create(**data)
    return schema.dump(m), 201

@mantenimiento_bp.route("/", methods=["GET"])
@jwt_required()
def list_mantenimientos():
    items = repo.get_all()
    return jsonify(schema.dump(items, many=True)), 200
