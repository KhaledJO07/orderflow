from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str]
    city: Optional[str]
    country: Optional[str]


class CustomerResponse(CustomerCreate):
    customer_id: int

    class Config:
        from_attributes = True