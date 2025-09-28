import os
from textwrap import dedent

# Lista de entidades de tu app de jardinería
ENTIDADES = [
    "usuario", "planta", "insumo", "producto", "carrito",
    "detalle_carrito", "pedido", "detalle_pedido", "mantenimiento",
    "foro", "comentario", "consejo", "jardin_virtual",
    "planta_jardin", "diseño"
]

# Carpeta donde se guardarán los archivos de rutas
ROUTES_DIR = os.path.join("src", "routes")

# Plantilla para cada archivo de rutas
ROUTE_TEMPLATE = """\
from flask import Blueprint, request, jsonify
from src.repositories.{entity}_repository import {Entity}Repository

{entity}_bp = Blueprint('{entity}_bp', __name__, url_prefix='/{entity_plural}')

repo = {Entity}Repository()

@{entity}_bp.route('/', methods=['GET'])
def listar_{entity_plural}():
    items = repo.get_all()
    return jsonify([item.__dict__ for item in items]), 200

@{entity}_bp.route('/<int:id>', methods=['GET'])
def obtener_{entity}(id):
    item = repo.get_by_id(id)
    if not item:
        return jsonify({{"error": "{Entity} no encontrado"}}), 404
    return jsonify(item.__dict__), 200

@{entity}_bp.route('/', methods=['POST'])
def crear_{entity}():
    data = request.json
    nuevo = repo.create(**data)
    return jsonify({{"message": "{Entity} creado", "id": nuevo.id}}), 201

@{entity}_bp.route('/<int:id>', methods=['PUT'])
def actualizar_{entity}(id):
    data = request.json
    actualizado = repo.update(id, **data)
    if not actualizado:
        return jsonify({{"error": "{Entity} no encontrado"}}), 404
    return jsonify({{"message": "{Entity} actualizado"}}), 200

@{entity}_bp.route('/<int:id>', methods=['DELETE'])
def eliminar_{entity}(id):
    eliminado = repo.delete(id)
    if not eliminado:
        return jsonify({{"error": "{Entity} no encontrado"}}), 404
    return jsonify({{"message": "{Entity} eliminado"}}), 200
"""

def generar_rutas():
    os.makedirs(ROUTES_DIR, exist_ok=True)

    for entidad in ENTIDADES:
        entity = entidad.lower()
        Entity = entidad.capitalize() if "_" not in entidad else "".join(p.capitalize() for p in entidad.split("_"))
        entity_plural = entity + "s"

        content = ROUTE_TEMPLATE.format(
            entity=entity,
            Entity=Entity,
            entity_plural=entity_plural
        )

        file_path = os.path.join(ROUTES_DIR, f"{entity}_routes.py")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(dedent(content))

        print(f"✅ Archivo generado: {file_path}")

if __name__ == "__main__":
    generar_rutas()
    print("\n🎉 Todas las rutas fueron generadas en src/routes/")
