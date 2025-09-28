# tests/test_jardin_virtual.py
def test_create_jardin_virtual(client):
    response = client.post("/jardines_virtuales", json={"usuario_id": 1, "nombre": "Mi jardín"})
    assert response.status_code == 201

def test_get_jardines_virtuales(client):
    response = client.get("/jardines_virtuales")
    assert response.status_code == 200
