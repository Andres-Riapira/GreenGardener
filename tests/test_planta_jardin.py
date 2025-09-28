# tests/test_planta_jardin.py
def test_create_planta_jardin(client):
    response = client.post("/plantas_jardin", json={"jardin_id": 1, "planta_id": 1})
    assert response.status_code == 201

def test_get_plantas_jardin(client):
    response = client.get("/plantas_jardin")
    assert response.status_code == 200
