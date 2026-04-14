from fastapi import APIRouter
from app.api.routes import customers, products, orders

api_router = APIRouter()

api_router.include_router(customers.router)
api_router.include_router(products.router)
api_router.include_router(orders.router)

@api_router.get("/health")
def health_check():
    return {"status": "healthy"}