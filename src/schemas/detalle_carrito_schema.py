# src/schemas/detalle_carrito_schema.py
from marshmallow import Schema, fields, validate

class DetalleCarritoSchema(Schema):
    id = fields.Int(dump_only=True)
    carrito_id = fields.Int(required=True)
    producto_id = fields.Int(required=True)
    cantidad = fields.Int(required=True, validate=validate.Range(min=1))
    precio_total = fields.Float(dump_only=True)
