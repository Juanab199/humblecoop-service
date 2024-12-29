from fastapi import APIRouter, Depends

from app.price_calculator.schemas.input_data import ItemsInput
from app.price_calculator.schemas.output_data import ItemsOutput
from app.db_controller.db_controller import DatabaseConnection, get_db_connection


router = APIRouter()

@router.post("/calculate-prices", response_model=ItemsOutput)
async def calculate_prices(data: ItemsInput, db_conection: DatabaseConnection = Depends(get_db_connection)):
    try:
        pass
    except Exception as e:
        pass