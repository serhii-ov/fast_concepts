from sqlalchemy.orm import Session, selectinload
from sqlmodel import select
from typing import Optional, List

from app.models.order import Order
from app.models.order_item import OrderItem
from app.schemas.order import OrderCreate, OrderUpdate


def create_order(db: Session, order_in: OrderCreate) -> Order:
    """Create a new order."""

    new_order = Order.model_validate(order_in)
    
    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


def get_order(db: Session, order_id: int,) -> Optional[Order]:
    """Get an order with specific id or None."""

    return db.get(Order, order_id)


def get_orders(
        db: Session, 
        skip: int = 0, 
        limit: int = 10,
        ) -> List[Order]:
    """Get all orders from DB."""

    return db.query(Order).offset(skip).limit(limit).all()


def update_order(
        db: Session, 
        order_id: int, 
        order_in: OrderUpdate,
        ) -> Optional[Order]:
    """Update existing order."""

    order = db.get(Order, order_id)
    if not order:
        return None
    
    data_to_update = order_in.model_dump(exclude_unset=True)

    for key, value in data_to_update.items():
        setattr(order, key, value)

    db.add(order)
    db.commit()
    db.refresh(order)

    return order


def delete_order(db: Session, order_id: int,) -> dict:
    """Delete an exiting order or return None."""

    order = db.get(Order, order_id)
    if not order: 
        return None
    
    db.delete(order)
    db.commit()

    return {"ok": "Order deleted successfully."}


def get_order_with_user_and_items(db: Session, order_id: int):
    """Get order's with a user who ordered and items."""

    statement = select(Order).where(Order.id==order_id).options(
        selectinload(Order.user),
        selectinload(Order.items).selectinload(OrderItem.product),
    )
    return db.exec(statement).first()
