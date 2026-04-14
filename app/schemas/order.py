from pydantic import BaseModel
from typing import List


class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    customer_id: int
    items: List[OrderItemCreate]


class OrderItemResponse(BaseModel):
    product_id: int
    quantity: int
    unit_price: float
    line_total: float

    class Config:
        from_attributes = True


class OrderResponse(BaseModel):
    order_id: int
    customer_id: int
    total_amount: float
    order_status: str
    payment_status: str
    items: List[OrderItemResponse]

    class Config:
        from_attributes = True