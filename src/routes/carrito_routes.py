from flask import Blueprint, jsonify, request

# src/routes/carrito_routes.py
from flask import Blueprint, request, jsonify
from src.repositories.carrito_repository import CarritoRepository
from src.schemas.carrito_schema import CarritoSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

carrito_bp = Blueprint("carrito", __name__)
repo = CarritoRepository()
schema = CarritoSchema()

@carrito_bp.route("/", methods=["POST"])
@jwt_required()
def create_carrito():
    user_id = get_jwt_identity()
    data = {"usuario_id": user_id}
    carrito = repo.create(**data)
    return schema.dump(carrito), 201

@carrito_bp.route("/", methods=["GET"])
@jwt_required()
def get_carritos():
    user_id = get_jwt_identity()
    carritos = repo.get_by_user(user_id)
    return jsonify(schema.dump(carritos, many=True)), 200
