from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime

from app.models.user import User
from app.schemas.user import (
    UserCreate, 
    UserUpdate,
    )


def create_user(
        db: Session, 
        user_in: UserCreate, 
        hashed_password: str,
        ) -> User:
    """Create a new user with hashed password."""

    new_user = User(
        username=user_in.username,
        email=user_in.email,
        full_name=user_in.full_name,
        role=user_in.role,
        hashed_password=hashed_password,
        is_active=True,
        created_at=datetime.now(),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user(db: Session, user_id: int,) -> User:
    return db.get(User, user_id,)


def get_user_by_username(
        db: Session, 
        username: str,
        ) -> Optional[User]:
    
    statement = select(User).where(User.username==username)
    return db.exec(statement).first()


def get_user_by_email(
        db: Session, email: str,
        ) -> Optional[User]:
    
    statement = select(User).where(User.email==email)
    return db.exec(statement).first()
