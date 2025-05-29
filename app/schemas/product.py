from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    in_stock: Optional[int] = 0


class ProductCreate(ProductBase):
    pass


class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    in_stock: Optional[int]    
