# src/routes/usuario_routes.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from src.repositories.usuario_repository import UsuarioRepository
from src.schemas.usuario_schema import UsuarioSchema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

usuario_bp = Blueprint("usuario", __name__)
repo = UsuarioRepository()
schema = UsuarioSchema()

@usuario_bp.route("/", methods=["POST"])
def register():
    data = request.get_json() or {}
    errors = schema.validate(data)
    if errors:
        return jsonify(errors), 400
    if repo.get_by_email(data["correo"]):
        return jsonify({"error":"Correo ya registrado"}), 400
    data["contrasena"] = generate_password_hash(data["contrasena"])
    user = repo.create(**data)
    return schema.dump(user), 201

@usuario_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    user = repo.get_by_email(data.get("correo"))
    if not user or not check_password_hash(user.contrasena, data.get("contrasena")):
        return jsonify({"error":"Credenciales inválidas"}), 401
    token = create_access_token(identity=user.id, additional_claims={"rol": user.rol})
    return jsonify({"access_token": token}), 200

@usuario_bp.route("/", methods=["GET"])
@jwt_required()
def list_users():
    users = repo.get_all()
    return jsonify(schema.dump(users, many=True)), 200

@usuario_bp.route("/<int:user_id>", methods=["GET"])
@jwt_required()
def get_user(user_id):
    user = repo.get_by_id(user_id)
    if not user:
        return jsonify({"error":"Usuario no encontrado"}), 404
    return schema.dump(user), 200
