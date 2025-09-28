from flask import Blueprint, request, jsonify
from src.repositories.diseno_repository import DisenoRepository

diseno_bp = Blueprint("diseno", __name__)

@diseno_bp.route("/", methods=["GET"])
def get_all_diseno():
    disenos = DisenoRepository.get_all()
    return jsonify([d.to_dict() for d in disenos])

