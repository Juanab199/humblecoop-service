import os
import pytest
from fastapi.testclient import TestClient

from app.price_calculator.manager import ProductsManager
from app.price_calculator.schemas.input_data import ItemInput, ItemsInput
from app.db.db_controller import get_db_connection
from app.main import app 


@pytest.fixture
def products_manager(db_connection):
    items_input = ItemsInput(items=[
        ItemInput(sku="123", provider="Provedor A", unitPrice=100),
        ItemInput(sku="124", provider="Provedor C", unitPrice=200)
    ])
    return ProductsManager(items=items_input.items, db_conection=db_connection)


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture(scope="module")
def db_connection():
    try:
        os.chdir("src")
    except:
        pass
    db_connection_gen = get_db_connection()
    db_connection = next(db_connection_gen)
    try:
        yield db_connection
    finally:
        db_connection_gen.close()
        
