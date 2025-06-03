from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .order_item import OrderItem


class Order(SQLModel):
    """Class represents user's order instance."""
    id: Optional[int] = Field(default=None, primary_key=True,)
    user_id: int = Field(foreign_key="user.id", nullable=False,)
    total_amount: float = Field(gt=0, nullable=False,)
    status: str = Field(default="pending", nullable=False,)
    created_at: datetime = Field(default_factory=datetime.now(),)
    updated_at: Optional[datetime] = Field(default=None)

    item: List["OrderItem"] = Relationship(back_populates="order")
