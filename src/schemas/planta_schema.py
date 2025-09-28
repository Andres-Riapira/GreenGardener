# src/schemas/planta_schema.py
from marshmallow import Schema, fields, validate

class PlantaSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre_comun = fields.Str(required=True, validate=validate.Length(min=2))
    nombre_cientifico = fields.Str()
    descripcion = fields.Str()
    req_luz = fields.Str()
    req_agua = fields.Str()
    req_suelo = fields.Str()
