# src/schemas/mantenimiento_schema.py
from marshmallow import Schema, fields, validate

class MantenimientoSchema(Schema):
    id = fields.Int(dump_only=True)
    usuario_id = fields.Int(required=True)
    fecha_solicitud = fields.DateTime(dump_only=True)
    estado = fields.Str(validate=validate.OneOf(["SOLICITADO", "EN_PROCESO", "FINALIZADO"]))
    descripcion = fields.Str()
