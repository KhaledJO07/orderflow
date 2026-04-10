from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.core.database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(50))
    city = Column(String(100))
    country = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())