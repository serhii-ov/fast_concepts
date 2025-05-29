from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List

from app.core.database import get_session
from app.schemas.product import (
                                ProductCreate, 
                                ProductRead, 
                                ProductUpdate,
                                )
from app.crud.product import (
                                create_product, 
                                get_product, 
                                get_products, 
                                update_product, 
                                delete_product,
                                )


router = APIRouter(prefix="/products", tags=["products"])


@router.post("/create", response_model=ProductRead)
def create(
    product: ProductCreate, 
    db: Session = Depends(get_session),
    ):
    return create_product(db, product)


@router.get("/", response_model=List[ProductRead])
def read_all(
    skip: int = 0, 
    limit: int = 10, 
    db: Session = Depends(get_session),
    ):
    return get_products(db, skip, limit)


@router.get("/{product_id}", response_model=ProductRead)
def read(
    product_id: int, 
    db: Session = Depends(get_session),
    ):

    product = get_product(db, product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product not found",
            )
    return product


@router.put("/{product_id}", response_model=ProductRead)
def update(
    product_id: int, 
    product_in: ProductUpdate, 
    db: Session = Depends(get_session),
    ):

    product = update_product(db, product_id, product_in)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product not found.",
            )
    return product


@router.delete("/{product_id}", response_model=ProductRead)
def delete(
    product_id: int, 
    db: Session = Depends(get_session),
    ):
    
    deleted_product = delete_product(db, product_id)
    if not deleted_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Product not found",
            )
    return {"ok": True,}
