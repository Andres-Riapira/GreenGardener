# src/routes/foro_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.foro_repository import ForoRepository
from src.schemas.foro_schema import ForoSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

foro_bp = Blueprint("foro", __name__)
repo = ForoRepository()
schema = ForoSchema()

@foro_bp.route("/", methods=["GET"])
def list_foros():
    return jsonify(schema.dump(repo.get_all(), many=True)), 200

@foro_bp.route("/", methods=["POST"])
@jwt_required()
def create_foro():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    data["usuario_id"] = user_id
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    f = repo.create(**data)
    return schema.dump(f), 201
