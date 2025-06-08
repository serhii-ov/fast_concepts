from pydantic import BaseModel, Field
from typing import Optional, Literal, List
from datetime import datetime

from app.schemas.user import UserNested
from app.schemas.order_item import OrderItemRead


class OrderBase(BaseModel):
    """Class represents base fields for all schemas."""
    total_amount: float = Field(..., gt=0,)
    status: Literal["pending", "paid", "shipped", "cancelled",] = "pending"


class OrderCreate(OrderBase):
    """Class represents required fields to create a new order."""
    order_id: int


class OrderUpdate(BaseModel):
    """Class represents fields allowed to update in order."""
    total_amount: Optional[float] = Field(None, gt=0,)
    status: Optional[Literal["pending", "paid", "shipped", "cancelled",]] = None


class OrderRead(BaseModel):
    """Class represents fields when returning to the client."""
    id: int
    user_id: int
    status: str
    cerated_at: datetime
    updated_at: Optional[datetime] = None

    user: UserNested
    items: List[OrderItemRead] = []

    class Config:
        orm_mode = True
