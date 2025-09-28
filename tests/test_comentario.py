# tests/test_comentario.py
def test_create_comentario(client):
    response = client.post("/comentarios", json={"foro_id": 1, "texto": "Muy buen consejo"})
    assert response.status_code == 201

def test_get_comentarios(client):
    response = client.get("/comentarios")
    assert response.status_code == 200
