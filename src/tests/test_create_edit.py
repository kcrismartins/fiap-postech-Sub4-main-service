import pytest
from httpx import AsyncClient
from src.main import app
from src.database import session
from src.models import Vehicle

@pytest.fixture(scope="module")
def test_client():
    return AsyncClient(app=app, base_url="http://test")

@pytest.fixture(scope="function", autouse=True)
def setup_database():
    session.query(Vehicle).delete()
    session.commit()

async def test_create_vehicle(test_client):
    vehicle_data = {"brand": "Ford", "model": "Fiesta", "year": 2022, "color": "Blue", "price": 15000}
    response = await test_client.post("/vehicles", json=vehicle_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Vehicle created successfully"

    # Verifica no banco de dados
    vehicle = session.query(Vehicle).filter_by(brand="Ford").first()
    assert vehicle is not None
    assert vehicle.price == 15000

async def test_edit_vehicle(test_client):
    vehicle_data = {"brand": "Ford", "model": "Fiesta", "year": 2022, "color": "Blue", "price": 15000}
    response = await test_client.post("/vehicles", json=vehicle_data)
    vehicle_id = response.json()["vehicle_id"]

    updated_data = {"price": 14000}
    response = await test_client.put(f"/vehicles/{vehicle_id}", json=updated_data)
    assert response.status_code == 200

    # Verifica no banco de dados
    vehicle = session.query(Vehicle).filter_by(id=vehicle_id).first()
    assert vehicle.price == 14000
