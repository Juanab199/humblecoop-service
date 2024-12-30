from fastapi import FastAPI

from app import SERVICE_VERSION
from app.price_calculator.entrypoint import router
from app.healthz.healthz import healthz_router


app: FastAPI = FastAPI(
    title="HumbleCoop Price API ",
    description="Calculadora de precios",
    docs_url="/v1/docs",
    version=SERVICE_VERSION,
)

app.include_router(router)
app.include_router(healthz_router)