# src/routes/consejo_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.consejo_repository import ConsejoRepository
from src.schemas.consejo_schema import ConsejoSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

consejo_bp = Blueprint("consejo", __name__)
repo = ConsejoRepository()
schema = ConsejoSchema()

@consejo_bp.route("/", methods=["GET"])
def list_consejos():
    return jsonify(schema.dump(repo.get_all(), many=True)), 200

@consejo_bp.route("/", methods=["POST"])
@jwt_required()
def create_consejo():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    data["usuario_id"] = user_id
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    c = repo.create(**data)
    return schema.dump(c), 201
