from fastapi import APIRouter
from app.price_calculator.schemas.input_data import ItemsInput
from app.price_calculator.schemas.output_data import ItemsOutput

router = APIRouter()

@router.post("/calculate-prices", response_model=ItemsOutput)
async def calculate_prices(data: ItemsInput):
    try:
        pass
    except Exception as e:
        pass