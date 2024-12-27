from pydantic import BaseModel, Field
from typing import List

class ItemOutput(BaseModel):
    sku: str
    unitPriceWithDiscount: float 

class ItemsOutput(BaseModel):
    items: List[ItemOutput]