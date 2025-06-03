from pydantic import BaseModel, Field
from typing import Optional

from app.schemas.product import ProductNested


class OrderItemBase(BaseModel):
    """Class represents shared base for OrderItem creation and update."""
    product_id: int = Field(..., description="ID of the product")
    quantity: int = Field(
                            ..., 
                            gt=0, 
                            description="Quantity of the product",
                        )
    unit_price: float = Field(
                                ..., 
                                gt=0, 
                                description="Unit price at time of order",
                            )


class OrderItemCreate(OrderItemBase):
    """Class represents schema for creating an OrderItem"""
    user_id: int = Field(..., description="ID of the user who owns the order",)


class OrderItemUpdate(BaseModel):
    """Class represents schema for OrderItem updating."""
    quantity: Optional[int] = Field(None, gt=0,)
    unit_price: Optional[float] =Field(None, gt=0,)


class OrderItemRead(BaseModel):
    """Class represents schema for OrderItem reading"""
    id: int
    user_id: int
    product: Optional[ProductNested]

    class Config:
        orm_mode = True
