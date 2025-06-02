from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.order import (
                                OrderCreate, 
                                OrderUpdate, 
                                OrderRead,
                                )
from app.crud.order import (
                            create_order, 
                            update_order, 
                            get_order, 
                            get_orders, 
                            delete_order,
                            )
from app.core.database import get_session


router = APIRouter("/orders", tags=["Orders"])


@router.post(
            "/", 
            response_model=OrderRead, 
            status_code=status.HTTP_201_CREATED,
            )
def create(
            order_in: OrderCreate, 
            db: Session = Depends(get_session),
            ):
    return create_order(db, order_in)


@router.get("/", response_model=OrderRead,)
def read_all(
            skip: int = 0, 
            limit: int = 10, 
            db: Session = Depends(get_session),
            ) -> List[OrderRead]:
    return get_orders(db, skip, limit)


@router.get("/{order_id}", response_model=OrderRead,)
def read(
        order_id: int, db: 
        Session = Depends(get_session),
        ):
    
    order = get_order(db, order_id)
    if not order: 
        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Order not found.",
                            )
    return order


@router.delete(
        "/{order_id}", 
        status_code=status.HTTP_204_NO_CONTENT,
        )
def delete(
    order_id: int, 
    db: Session = Depends(get_session),
    ):
    success = delete_order(db, order_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found."
        )
    return {"ok": "Order deleted successfully."}
