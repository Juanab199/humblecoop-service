from fastapi import FastAPI

from app import SERVICE_VERSION


app: FastAPI = FastAPI(
    title="HumbleCoop Price API ",
    description="Calculadora de precios",
    docs_url="/v1/docs",
    version=SERVICE_VERSION,
)
