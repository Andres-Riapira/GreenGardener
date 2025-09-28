# tests/test_usuario.py
def test_create_usuario(client):
    response = client.post("/usuarios", json={
        "nombre": "Carlos",
        "email": "carlos@test.com",
        "password": "1234"
    })
    assert response.status_code == 201
    assert "id" in response.json

def test_get_usuarios(client):
    response = client.get("/usuarios")
    assert response.status_code == 200
