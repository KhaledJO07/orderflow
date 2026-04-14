from sqlalchemy.orm import Session
from app.models.payment import Payment
from app.models.order import Order
from app.schemas.payment import PaymentCreate
import random

def create_payment(db: Session, payment_data: PaymentCreate):
    # Validate order
    order = db.query(Order).filter(Order.order_id == payment_data.order_id).first()
    if not order:
        raise ValueError("Order not found")

    # Simulate payment result
    payment_status = random.choice(["success", "failed"])

    db_payment = Payment(
        order_id=payment_data.order_id,
        payment_method=payment_data.payment_method,
        payment_status=payment_status,
        payment_amount=payment_data.payment_amount,
        transaction_reference=f"TXN{random.randint(100000,999999)}"
    )

    db.add(db_payment)

    # Update order payment status
    order.payment_status = "paid" if payment_status == "success" else "failed"

    db.commit()
    db.refresh(db_payment)

    return db_payment