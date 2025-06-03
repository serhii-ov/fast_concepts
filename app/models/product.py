from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING

if TYPE_CHECKING:
    from .order_item import OrderItem


class Product(SQLModel):
    """Class represents product instance."""

    id: Optional[int] = Field(default=None, primary_key=True,)
    name: str = Field(index=True, nullable=False,)
    description: Optional[str] = None
    price: float = Field(nullable=False)
    in_stock: int = Field(default=0)

    order_item: List["OrderItem"] = Relationship(back_populates="product")
