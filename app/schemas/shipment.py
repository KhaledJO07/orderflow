from pydantic import BaseModel
from typing import Optional


class ShipmentCreate(BaseModel):
    order_id: int
    carrier: str


class ShipmentResponse(BaseModel):
    shipment_id: int
    order_id: int
    shipment_status: str
    carrier: str
    tracking_number: Optional[str]

    class Config:
        from_attributes = True