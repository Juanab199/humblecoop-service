from app.price_calculator.models.db_models import HumbleProviders
from app.db_controller.db_controller import DatabaseConnection

class ProductsManager:
    def __init__(self, sku: str, price: float, provider: str):
        self._sku = sku
        self._price = price
        self._provider = provider
        
    def get_discount_from_provider(self, db_conection: DatabaseConnection):
        provider_registry: HumbleProviders = db_conection.get_db_registry_by_column("name", self._provider, HumbleProviders)
        self._provider_discount = provider_registry.discount
        
    def calculate_discounted_price(self):
        return self._price * self._provider_discount
        
        