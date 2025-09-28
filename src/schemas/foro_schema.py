# src/schemas/foro_schema.py
from marshmallow import Schema, fields, validate

class ForoSchema(Schema):
    id = fields.Int(dump_only=True)
    titulo = fields.Str(required=True, validate=validate.Length(min=3))
    descripcion = fields.Str()
    fecha_creacion = fields.DateTime(dump_only=True)
    usuario_id = fields.Int(required=True)
