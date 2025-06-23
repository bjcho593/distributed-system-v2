from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_profile():
    payload = {
        "user_id": "u456",
        "name": "Tester",
        "email": "tester@example.com",
        "bio": "Testing profile"
    }

    # Crear perfil
    response = client.post("/profile/", json=payload)
    assert response.status_code in [200, 201, 409]  # Puede ya existir

    # Obtener perfil
    response = client.get("/profile/u456")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == "u456"
    assert data["email"] == "tester@example.com"
