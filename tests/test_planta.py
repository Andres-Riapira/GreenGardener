# tests/test_planta.py
def test_create_planta(client):
    response = client.post("/plantas", json={"nombre": "Rosa", "descripcion": "Flor bonita"})
    assert response.status_code == 201

def test_get_plantas(client):
    response = client.get("/plantas")
    assert response.status_code == 200