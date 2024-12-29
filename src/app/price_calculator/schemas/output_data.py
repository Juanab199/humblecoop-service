from pydantic import BaseModel
from typing import List, Optional

class ItemOutput(BaseModel):
    sku: str
    unitPriceWithDiscount: Optional[float]
    error: Optional[str]

class ItemsOutput(BaseModel):
    items: List[ItemOutput]