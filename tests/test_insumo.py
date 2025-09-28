# tests/test_insumo.py
def test_create_insumo(client):
    response = client.post("/insumos", json={"nombre": "Abono", "stock": 20})
    assert response.status_code == 201

def test_get_insumos(client):
    response = client.get("/insumos")
    assert response.status_code == 200
