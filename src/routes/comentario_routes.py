# src/routes/comentario_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.comentario_repository import ComentarioRepository
from src.schemas.comentario_schema import ComentarioSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

comentario_bp = Blueprint("comentario", __name__)
repo = ComentarioRepository()
schema = ComentarioSchema()

@comentario_bp.route("/", methods=["GET"])
def list_comentarios():
    return jsonify(schema.dump(repo.get_all(), many=True)), 200

@comentario_bp.route("/", methods=["POST"])
@jwt_required()
def create_comentario():
    user_id = get_jwt_identity()
    data = request.get_json() or {}
    data["usuario_id"] = user_id
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    c = repo.create(**data)
    return schema.dump(c), 201
