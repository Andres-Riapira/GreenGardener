# src/schemas/usuario_schema.py
from marshmallow import Schema, fields, validate

class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True, validate=validate.Length(min=2))
    correo = fields.Email(required=True)
    contrasena = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
    rol = fields.Str()
    fecha_creacion = fields.DateTime(dump_only=True)
