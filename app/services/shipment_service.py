from sqlalchemy.orm import Session
from app.models.shipment import Shipment
from app.models.order import Order
from app.schemas.shipment import ShipmentCreate
import random

def create_shipment(db: Session, shipment_data: ShipmentCreate):
    # Validate order
    order = db.query(Order).filter(Order.order_id == shipment_data.order_id).first()
    if not order:
        raise ValueError("Order not found")

    tracking_number = f"TRK{random.randint(100000,999999)}"

    db_shipment = Shipment(
        order_id=shipment_data.order_id,
        carrier=shipment_data.carrier,
        shipment_status="processing",
        tracking_number=tracking_number
    )

    db.add(db_shipment)

    # Update order status
    order.order_status = "processing"

    db.commit()
    db.refresh(db_shipment)

    return db_shipment