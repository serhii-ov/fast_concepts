from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class CartItemBase(BaseModel):
    """Class represents shared base for CartItem creation and reading."""
    product_id: int 
    quantity: int = Field(gt=0, default=1)


class CartItemCreate(CartItemBase):
    """Class represents schema for creating a CartItem"""
    pass


class CartItemRead(CartItemBase):
    """Class represents schema for CartItem reading"""
    id: int
    added_at: datetime

    class Config:
        orm_mode = True


class CartBase(BaseModel):
    """Class represents schema for creating and reading Cart"""
    user_id: int


class CartCreate(CartBase):
    """Class represents schema for creating a Cart"""
    pass


class CartRead(CartBase):
    """Class represents schema for Cart reading"""
    id: int

    created_at: datetime
    items: List[CartItemRead]

    class Config: 
        orm_mode = True
