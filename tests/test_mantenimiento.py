# tests/test_mantenimiento.py
def test_create_mantenimiento(client):
    response = client.post("/mantenimientos", json={"planta_id": 1, "descripcion": "Riego semanal"})
    assert response.status_code == 201

def test_get_mantenimientos(client):
    response = client.get("/mantenimientos")
    assert response.status_code == 200
