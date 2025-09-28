# src/schemas/comentario_schema.py
from marshmallow import Schema, fields, validate

class ComentarioSchema(Schema):
    id = fields.Int(dump_only=True)
    foro_id = fields.Int(required=True)
    usuario_id = fields.Int(required=True)
    contenido = fields.Str(required=True, validate=validate.Length(min=2))
    fecha_comentario = fields.DateTime(dump_only=True)
