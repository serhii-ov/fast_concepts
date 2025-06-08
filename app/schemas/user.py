from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional, Literal


# Role Support
class Role(str):
    """Class represents enum-like roles for users."""
    ADMIN = "admin"
    CUSTOMER = "customer"
    SELLER = "seller"


# Base + Creation + Update Schemas
class BaseUser(BaseModel):
    """Class represents base fields shared accross schemas."""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None
    role: Literal["admin", "customer", "seller"] = "customer"


class UserCreate(BaseUser):
    """Class represents new user."""
    password: str = Field(..., min_length=8)


class UserUpdate(BaseModel):
    """Used when updating a user."""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = Field(None, min_length=8)
    role: Optional[Literal["admin", "customer", "seller"]] = None


# DB + Response Schemas
class UserInDB(BaseUser):
    """Schema for internal DB representation (e.g., including hashed password)."""
    id: int
    hashed_password: str
    is_active: bool = True
    created_at: datetime

    class Config:
        orm_mode = True


class UserResponse(BaseUser):
    """Used when returning user data to client (excluding password)."""
    id: int
    is_active: bool = True
    created_at: datetime

    class Config:
        orm_mode = True


class UserNested(BaseModel):
    """Used in order response reading"""
    id: int
    username: str
    email: EmailStr
    full_name: str | None = None

    class Config:
        orm_mode = True


# Login & Token Support
class UserLogin(BaseModel):
    """Used when logging in."""
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    sub: str  # Usually the user ID or username
    exp: int
    role: Optional[str] = None
