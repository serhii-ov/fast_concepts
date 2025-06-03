from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .order import Order
    from .product import Product


class OrderItem(SQLModel, table=True):
    """Class represents an individual product in an order."""

    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", nullable=False)
    product_id: int = Field(foreign_key="product.id", nullable=False)

    quantity: int = Field(..., gt=0,)
    unit_price: float = Field(..., gt=0)

    order: Optional["Order"] = Relationship(back_populates="items")
    product: Optional["Product"] = Relationship(back_populates="order_items")
