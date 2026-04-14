from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import engine
from sqlalchemy.orm import declarative_base
from app.models.base import Base

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))
    order_date = Column(TIMESTAMP, server_default=func.now())
    order_status = Column(String(50))
    total_amount = Column(Numeric(10, 2))
    payment_status = Column(String(50))