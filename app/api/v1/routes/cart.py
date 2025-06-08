from fastapi import (
                    APIRouter, 
                    Depends, 
                    HTTPException, 
                    status,
                    )
from sqlalchemy.orm import Session
from typing import List

from app.schemas.cart import (
                            CartCreate, 
                            CartRead, 
                            CartItemCreate, 
                            CartItemRead,
                            )
from app.crud.cart import (
                            create_cart, 
                            get_cart, 
                            add_cart_item, 
                            get_cart_items, 
                            remove_cart_item,
                            )
from app.core.database import get_session


router = APIRouter(prefix="/cart", tags=["Cart"],)


@router.post("/", response_model=CartRead)
def create_cart(
            cart_in: CartCreate, 
            db: Session = Depends(get_session),
            ):
    """Create a new cart."""
    return create_cart(db, cart_in)


@router.get("/{cart_id}", response_model=CartRead,)
def read_cart(
    cart_id: int, 
    db: Session = Depends(get_session),
    ):
    """Get info from a cart."""

    cart = read_cart(db, cart_id)
    if not cart:
        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Cart not found",
                            )
    cart.items = get_cart_items(db, cart_id)

    return cart


@router.post("/{item_id}/items", response_model=CartItemRead)
def add_item(
            cart_id: int, 
            item_in: CartItemCreate, 
            db: Session = Depends(get_session),
            ):
    """Add a new item."""

    return add_cart_item(db, cart_id, item_in)


@router.delete(
                "/items/{item_id}", 
                status_code=status.HTTP_204_NO_CONTENT,
                )
def delete_item(item_id: int, db: Session = Depends(get_session)):
    """Delete item from the cart by its id."""

    remove_cart_item(db, item_id)
    return {"ok": "Item deleted successfully."}
