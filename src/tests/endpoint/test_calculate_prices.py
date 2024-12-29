import pytest
from fastapi.testclient import TestClient
from app.db_controller.db_controller import DatabaseConnection, get_db_connection
from app.price_calculator.schemas.input_data import ItemsInput, ItemInput
from app.main import app  # Asumimos que la app está en un archivo main.py


def test_calculate_prices(client):
    items_input = ItemsInput(
        items=[
            ItemInput(sku='123', unitPrice=10, provider= "Provedor A"),
            ItemInput(sku='123', unitPrice=15, provider= "Provedor B")
        ]
    )
    
    response = client.post("/calculate-prices", json=items_input.model_dump())
    assert response.status_code == 200
    data = response.json()
    assert len(data["items"]) == 2
    assert "sku" in data["items"][0]
    assert "unitPriceWithDiscount" in data["items"][0]
    assert data["items"][0]["error"] == None


def test_calculate_prices_invalid_provider(client):
    items_input = ItemsInput(
        items=[
            ItemInput(sku='123', unitPrice=10, provider= "Provedor Z"),
        ]
    )
    
    response = client.post("/calculate-prices", json=items_input.model_dump())
    assert response.status_code == 400
    assert "Provider not found" in response.json()["detail"]