# src/schemas/consejo_schema.py
from marshmallow import Schema, fields, validate

class ConsejoSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True, validate=validate.Length(min=3))
    categoria = fields.Str()
    contenido = fields.Str(required=True)
    planta_id = fields.Int(allow_none=True)
    usuario_id = fields.Int(required=True)
