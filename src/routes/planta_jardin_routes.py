# src/routes/planta_jardin_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.planta_jardin_repository import PlantaJardinRepository
from src.schemas.planta_jardin_schema import PlantaJardinSchema
from flask_jwt_extended import jwt_required

planta_jardin_bp = Blueprint("planta_jardin", __name__)
repo = PlantaJardinRepository()
schema = PlantaJardinSchema()

@planta_jardin_bp.route("/", methods=["POST"])
@jwt_required()
def add_planta_jardin():
    data = request.get_json() or {}
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    pj = repo.create(**data)
    return schema.dump(pj), 201

@planta_jardin_bp.route("/", methods=["GET"])
@jwt_required()
def list_planta_jardin():
    items = repo.get_all()
    return jsonify(schema.dump(items, many=True)), 200
