from abc import ABC, abstractmethod

from app.price_calculator.models.db_models import HumbleProviders
from app.price_calculator.schemas.input_data import ItemsInput, ItemInput
from app.price_calculator.schemas.output_data import ItemOutput
from app.db_controller.db_controller import DatabaseConnection


class IProvidersManager(ABC):
    @abstractmethod
    def fetch_providers_data(self, provider_names: list) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_providers_discounts(self) -> dict:
        raise NotImplementedError
    
    
class ProvidersManager(IProvidersManager):
    def __init__(self, db_conection):
        self._providers_data: list[HumbleProviders] = []
        self.db_conection: DatabaseConnection = db_conection
             
    def fetch_providers_data(self, provider_names: list) -> None:
        self._providers_data = self.db_conection.get_db_registries_by_column(
            column="name",
            values=provider_names,
            table=HumbleProviders
        )

    def get_providers_discounts(self) -> list[float]:
        return {provider.name: provider.discount for provider in self._providers_data}


class ProductsManager:
    def __init__(self, items: ItemsInput, db_conection: DatabaseConnection):
        self._providers_manager = ProvidersManager(db_conection)
        self._items = items
        self._provider_discounts: dict
        self._results: list = []
        
    def _get_provider_discounts(self):
            provider_names = list({item.provider for item in self._items})
            self._providers_manager.fetch_providers_data(provider_names)
            self._provider_discounts = self._providers_manager.get_providers_discounts()
        
    def _process_item(self, item: ItemInput) -> dict:
        provider_name = item.provider
        unit_price = item.unitPrice

        discount = self._provider_discounts[provider_name]
        discounted_price = unit_price * discount

        return ItemOutput(
            sku = item.sku,
            unitPriceWithDiscount = discounted_price,
        )
    
    def process_items(self):
        self._get_provider_discounts()
        self._results = [self._process_item(item) for item in self._items]
    
    def get_results(self) -> list[ItemOutput]:
        return self._results