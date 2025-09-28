# tests/test_consejo.py
def test_create_consejo(client):
    response = client.post("/consejos", json={"titulo": "Riego correcto", "contenido": "2 veces por semana"})
    assert response.status_code == 201

def test_get_consejos(client):
    response = client.get("/consejos")
    assert response.status_code == 200
