# tests/test_detalle_carrito.py
def test_create_detalle_carrito(client):
    response = client.post("/detalles_carrito", json={"carrito_id": 1, "producto_id": 1, "cantidad": 2})
    assert response.status_code == 201

def test_get_detalles_carrito(client):
    response = client.get("/detalles_carrito")
    assert response.status_code == 200
