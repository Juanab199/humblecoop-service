from fastapi import APIRouter, Depends, HTTPException

from app.price_calculator.schemas.input_data import ItemsInput
from app.price_calculator.schemas.output_data import ItemsOutput
from app.price_calculator.manager import ProductsManager
from app.db.db_controller import DatabaseConnection, get_db_connection
from app.exceptions.exceptions import NotRegistryFound


router = APIRouter()

@router.post("/calculate-prices", response_model=ItemsOutput)
async def calculate_prices(
    data: ItemsInput, db_connection: DatabaseConnection = Depends(get_db_connection)
):
    try:
        products_manager = ProductsManager(
            items=data.items,
            db_conection=db_connection,
        )

        products_manager.process_items()

        return ItemsOutput(items=products_manager.get_results())
    
    except NotRegistryFound:
        raise HTTPException(
            status_code=400,
            detail="Provider not found"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))