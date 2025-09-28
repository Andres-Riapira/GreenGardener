# src/schemas/pedido_schema.py
from marshmallow import Schema, fields, validate

class PedidoSchema(Schema):
    id = fields.Int(dump_only=True)
    usuario_id = fields.Int(required=True)
    fecha_pedido = fields.DateTime(dump_only=True)
    estado = fields.Str(validate=validate.OneOf(["PENDIENTE", "ENVIADO", "CANCELADO"]))
