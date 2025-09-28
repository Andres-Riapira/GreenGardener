# src/schemas/insumo_schema.py
from marshmallow import Schema, fields, validate

class InsumoSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=2))
    descripcion = fields.Str()
    precio = fields.Float(required=True, validate=validate.Range(min=0))
