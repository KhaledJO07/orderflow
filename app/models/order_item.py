from sqlalchemy import Column, Integer, ForeignKey, Numeric
from app.core.database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class OrderItem(Base):
    __tablename__ = "order_items"

    order_item_id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    quantity = Column(Integer)
    unit_price = Column(Numeric(10, 2))
    line_total = Column(Numeric(10, 2))