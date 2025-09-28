# src/schemas/carrito_schema.py
from marshmallow import Schema, fields

class CarritoSchema(Schema):
    id = fields.Int(dump_only=True)
    usuario_id = fields.Int(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)
