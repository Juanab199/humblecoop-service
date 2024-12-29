from pydantic import BaseModel
from typing import List

class ItemOutput(BaseModel):
    sku: str
    unitPriceWithDiscount: float

class ItemsOutput(BaseModel):
    items: List[ItemOutput]