from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime 


class User(SQLModel, table=True):
    """Class represents user instance."""

    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, nullable=False)
    email: str = Field(unique=True, nullable=False)
    full_name: Optional[str]
    hashed_password: str
    role: str = "customer"
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now())
