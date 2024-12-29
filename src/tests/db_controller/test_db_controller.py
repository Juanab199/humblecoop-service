import pytest
from app.db.db_controller import DatabaseConnection
from app.price_calculator.models.db_models import HumbleProviders
from app.exceptions.exceptions import NotRegistryFound


def test_get_db_registry_by_id(db_connection: DatabaseConnection):
    provider = db_connection.get_db_registry_by_id(1, HumbleProviders)
    assert provider is not None
    assert provider.id == 1


def test_get_db_registries_by_column(db_connection: DatabaseConnection):
    providers = db_connection.get_db_registries_by_column("provider_name", ["Provedor A", "Provedor B"], HumbleProviders)
    assert len(providers) > 0
    assert all(provider.provider_name in ["Provedor A", "Provedor B"] for provider in providers)


def test_get_db_registry_by_invalid_id(db_connection:DatabaseConnection):
    with pytest.raises(NotRegistryFound):
        db_connection.get_db_registries_by_column("provider_name", ["Provedor Z"], HumbleProviders)