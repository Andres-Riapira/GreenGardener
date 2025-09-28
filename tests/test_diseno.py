# tests/test_diseno.py
def test_create_diseno(client):
    response = client.post("/disenos", json={"nombre": "Diseño Zen"})
    assert response.status_code == 201

def test_get_disenos(client):
    response = client.get("/disenos")
    assert response.status_code == 200
