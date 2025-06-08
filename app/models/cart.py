from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .product import Product


class Cart(SQLModel, table=True):
    """Class represents cart instance."""

    id: Optional[int] = Field(default=None, primary_key=True,)
    user_id: int = Field(foreign_key="user.id",nullable=False)
    created_at: datetime = Field(default_factory=datetime.now())

    items: List["CartItem"] = Relationship(back_populates="cart")


class CartItem(SQLModel, table=True):
    """Class represent cart item instance."""
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="cart.id", nullable=False)
    product_id: int = Field(foreign_key="product.id", nullable=False)
    quantity: int = Field(gt=0, default=1)
    added_at: datetime = Field(default_factory=datetime.now()) 

    cart: Optional[Cart] = Relationship(back_populates="items")
    product: Optional["Product"] = Relationship()
