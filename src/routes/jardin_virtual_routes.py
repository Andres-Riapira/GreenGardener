# src/routes/jardin_virtual_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.jardin_virtual_repository import JardinVirtualRepository
from src.schemas.jardin_virtual_schema import JardinVirtualSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

jardin_virtual_bp = Blueprint("jardin_virtual", __name__)
repo = JardinVirtualRepository()
schema = JardinVirtualSchema()

@jardin_virtual_bp.route("/", methods=["GET"])
def list_jardines():
    return jsonify(schema.dump(repo.get_all(), many=True)), 200

@jardin_virtual_bp.route("/", methods=["POST"])
@jwt_required()
def create_jardin():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    data["usuario_id"] = user_id
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    j = repo.create(**data)
    return schema.dump(j), 201
