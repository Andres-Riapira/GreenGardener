# src/routes/planta_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.planta_repository import PlantaRepository
from src.schemas.planta_schema import PlantaSchema
from flask_jwt_extended import jwt_required

planta_bp = Blueprint("planta", __name__)
repo = PlantaRepository()
schema = PlantaSchema()

@planta_bp.route("/", methods=["GET"])
def list_plantas():
    plantas = repo.get_all()
    return jsonify(schema.dump(plantas, many=True)), 200

@planta_bp.route("/", methods=["POST"])
@jwt_required()
def create_planta():
    data = request.get_json() or {}
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    p = repo.create(**data)
    return schema.dump(p), 201

@planta_bp.route("/<int:pid>", methods=["GET"])
def get_planta(pid):
    p = repo.get_by_id(pid)
    if not p:
        return jsonify({"error":"Planta no encontrada"}), 404
    return schema.dump(p), 200
