from app.price_calculator.schemas.input_data import ItemInput, ItemsInput
from app.price_calculator.schemas.output_data import ItemOutput
from app.price_calculator.products import ProductsManager

def test_process_items(products_manager: ProductsManager):
    products_manager.process_items()
    results = products_manager.get_results()
    assert len(results) == 2
    assert isinstance(results[0], ItemOutput)
    assert results[0].unitPriceWithDiscount is not None


def test_process_item_with_invalid_provider(products_manager: ProductsManager):
    valid_item = ItemInput(sku="125", provider="Provedor A", unitPrice=150)
    invalid_item = ItemInput(sku="125", provider="Provedor Z", unitPrice=150)
    products_manager._items = [invalid_item, valid_item]
    products_manager.process_items()
    result = products_manager.get_results()[0]
    assert result.error == "Provider 'Provedor Z' not found"