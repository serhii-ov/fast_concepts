from sqlmodel import Session, select
from typing import List, Optional

from app.schemas.cart import CartCreate, CartItemCreate
from app.models.cart import Cart, CartItem


def create_cart(db: Session, cart_in: CartCreate) -> Cart:
    """Create a new cart."""

    cart = Cart(**cart_in.model_dump())

    db.add(cart)
    db.commit()
    db.refresh(cart)

    return cart


def get_cart(db: Session, cart_id: int) -> Optional[Cart]:
    """Get a cart by its id."""

    statement = select(Cart).where(Cart.id==cart_id)
    return db.exec(statement).first()


def add_cart_item(
                db: Session, 
                cart_id: int, 
                item_in: CartItemCreate,
                ) -> CartItem:
    """Add a new cart item."""

    cart_item = CartItem(
                        cart_id=cart_id, 
                        **item_in.model_dump(),
                        )
    db.add(cart_item)
    db.commit()
    db.refresh(cart_item)

    return cart_item


def get_cart_items(db: Session, cart_id: int) -> List[CartItem]:
    """Get all items from specific cart."""

    statement = select(CartItem).where(CartItem.cart_id==cart_id)
    return list(db.exec(statement))


def remove_cart_item(db: Session, item_id: int):
    """Remove a cart item by its id."""
    item_to_remove = db.get(CartItem, item_id)

    if item_to_remove:
        db.delete(item_to_remove)
        db.commit()

