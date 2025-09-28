# src/schemas/detalle_pedido_schema.py
from marshmallow import Schema, fields, validate

class DetallePedidoSchema(Schema):
    id = fields.Int(dump_only=True)
    pedido_id = fields.Int(required=True)
    producto_id = fields.Int(required=True)
    cantidad = fields.Int(required=True, validate=validate.Range(min=1))
    precio_total = fields.Float(dump_only=True)
