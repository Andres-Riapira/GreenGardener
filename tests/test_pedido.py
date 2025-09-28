# tests/test_pedido.py
def test_create_pedido(client):
    response = client.post("/pedidos", json={"usuario_id": 1, "total": 50})
    assert response.status_code == 201

def test_get_pedidos(client):
    response = client.get("/pedidos")
    assert response.status_code == 200
