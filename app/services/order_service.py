from sqlalchemy.orm import Session
from app.models.order import Order
from app.models.product import Product
from app.models.customer import Customer
from app.models.order_item import OrderItem
from app.schemas.order import OrderCreate

def create_order(db: Session, order_data: OrderCreate):
    # 1. Validate customer
    customer = db.query(Customer).filter(Customer.customer_id == order_data.customer_id).first()
    if not customer:
        raise ValueError("Customer not found")

    total_amount = 0
    order_items = []

    # 2. Process items
    for item in order_data.items:
        product = db.query(Product).filter(Product.product_id == item.product_id).first()
        if not product:
            raise ValueError(f"Product {item.product_id} not found")

        unit_price = float(product.price)
        line_total = unit_price * item.quantity

        total_amount += line_total

        order_items.append({
            "product_id": item.product_id,
            "quantity": item.quantity,
            "unit_price": unit_price,
            "line_total": line_total
        })

    # 3. Create order
    db_order = Order(
        customer_id=order_data.customer_id,
        total_amount=total_amount,
        order_status="pending",
        payment_status="unpaid"
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    # 4. Insert order items
    created_items = []
    for item in order_items:
        db_item = OrderItem(
            order_id=db_order.order_id,
            **item
        )
        db.add(db_item)
        created_items.append(db_item)

    db.commit()

    return {
        "order_id": db_order.order_id,
        "customer_id": db_order.customer_id,
        "total_amount": total_amount,
        "order_status": db_order.order_status,
        "payment_status": db_order.payment_status,
        "items": created_items
    }