# src/schemas/producto_schema.py
from marshmallow import Schema, fields, validate

class ProductoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=2))
    descripcion = fields.Str()
    precio = fields.Float(required=True, validate=validate.Range(min=0))
    categoria = fields.Str()
    planta_id = fields.Int(allow_none=True)
    insumo_id = fields.Int(allow_none=True)
