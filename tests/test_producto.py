# tests/test_producto.py
def test_create_producto(client):
    response = client.post("/productos", json={"nombre": "Maceta", "precio": 15.5})
    assert response.status_code == 201

def test_get_productos(client):
    response = client.get("/productos")
    assert response.status_code == 200
