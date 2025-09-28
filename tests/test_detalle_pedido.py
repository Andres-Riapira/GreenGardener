# tests/test_detalle_pedido.py
def test_create_detalle_pedido(client):
    response = client.post("/detalles_pedido", json={"pedido_id": 1, "producto_id": 1, "cantidad": 3})
    assert response.status_code == 201

def test_get_detalles_pedido(client):
    response = client.get("/detalles_pedido")
    assert response.status_code == 200
