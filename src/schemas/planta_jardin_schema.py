# src/schemas/planta_jardin_schema.py
from marshmallow import Schema, fields

class PlantaJardinSchema(Schema):
    id = fields.Int(dump_only=True)
    jardin_id = fields.Int(required=True)
    planta_id = fields.Int(required=True)
    pos_x = fields.Int()
    pos_y = fields.Int()
    fecha_plantacion = fields.Date()
