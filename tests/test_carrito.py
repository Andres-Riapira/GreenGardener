# tests/test_carrito.py
def test_create_carrito(client):
    response = client.post("/carritos", json={"usuario_id": 1})
    assert response.status_code == 201

def test_get_carritos(client):
    response = client.get("/carritos")
    assert response.status_code == 200
