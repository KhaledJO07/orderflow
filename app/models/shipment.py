from sqlalchemy import Column, Integer, ForeignKey, String, TIMESTAMP
from app.models.base import Base

class Shipment(Base):
    __tablename__ = "shipments"

    shipment_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    shipment_status = Column(String(50))
    carrier = Column(String(100))
    tracking_number = Column(String(255))
    shipped_date = Column(TIMESTAMP)
    delivered_date = Column(TIMESTAMP)