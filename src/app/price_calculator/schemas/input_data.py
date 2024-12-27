from pydantic import BaseModel, Field
from typing import List

class ItemInput(BaseModel):
    sku: str 
    unitPrice: float
    provider: str

class ItemsInput(BaseModel):
    items: List[ItemInput]