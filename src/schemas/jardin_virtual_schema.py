# src/schemas/jardin_virtual_schema.py
from marshmallow import Schema, fields, validate

class JardinVirtualSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=2))
    descripcion = fields.Str()
    usuario_id = fields.Int(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)
