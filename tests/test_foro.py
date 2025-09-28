# tests/test_foro.py
def test_create_foro(client):
    response = client.post("/foros", json={"titulo": "Cuidado de cactus"})
    assert response.status_code == 201

def test_get_foros(client):
    response = client.get("/foros")
    assert response.status_code == 200
