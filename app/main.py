from fastapi import FastAPI
from app.api.router import api_router
from app.models import customer, product, order, order_item

app = FastAPI(
    title="OrderFlow API",
    description="Backend API for E-Commerce Operations",
    version="1.0.0"
)

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "OrderFlow API is running"}