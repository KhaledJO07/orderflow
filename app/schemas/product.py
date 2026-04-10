from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    product_name: str
    category: Optional[str]
    price: float
    stock_quantity: int
    is_active: Optional[bool] = True


class ProductResponse(ProductCreate):
    product_id: int

    class Config:
        from_attributes = True