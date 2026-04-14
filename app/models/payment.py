from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, TIMESTAMP
from sqlalchemy.sql import func
from app.models.base import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    payment_method = Column(String(50))
    payment_status = Column(String(50))
    payment_amount = Column(Numeric(10, 2))
    payment_date = Column(TIMESTAMP, server_default=func.now())
    transaction_reference = Column(String(255))