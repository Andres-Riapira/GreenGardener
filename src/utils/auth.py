# src/utils/auth.py
import datetime
import jwt
from flask import request, jsonify
from functools import wraps
from src.config import Config

SECRET_KEY = Config.JWT_SECRET_KEY

def generate_token(user_id, role, expires_hours: int = 1):
    payload = {
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=expires_hours),
        "iat": datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]
        if not token:
            return jsonify({"error": "Token requerido"}), 401
        data = decode_token(token)
        if not data:
            return jsonify({"error": "Token inválido o expirado"}), 401
        return f(*args, **kwargs, current_user=data)
    return decorated

def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if "Authorization" in request.headers:
                auth_header = request.headers["Authorization"]
                if auth_header.startswith("Bearer "):
                    token = auth_header.split(" ")[1]
            if not token:
                return jsonify({"error": "Token requerido"}), 401
            data = decode_token(token)
            if not data:
                return jsonify({"error": "Token inválido o expirado"}), 401
            if data.get("role") != role:
                return jsonify({"error": "No tienes permisos para acceder"}), 403
            return f(*args, **kwargs, current_user=data)
        return decorated
    return wrapper
