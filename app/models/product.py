from sqlmodel import SQLModel, Field
from typing import Optional


class Product(SQLModel):
    """Class represents product instance."""

    id: Optional[int] = Field(default=None, primary_key=True,)
    name: str = Field(index=True, nullable=False,)
    description: Optional[str] = None
    price: float = Field(nullable=False)
    in_stock: int = Field(default=0)
