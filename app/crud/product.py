from sqlmodel import Session, select
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

from typing import Optional, List


def create_product(
        db: Session, 
        product_in: ProductCreate,
        ) -> Product:
    
    product = Product(**product_in.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_product(
        db: Session, 
        product_id: int,
        ) -> Optional[Product]:
    
    return db.get(Product, product_id)


def get_products(
        db: Session, 
        skip: int = 0, 
        limit: int = 10,
        ) -> List[Product]:
    
    return db.exec(select(Product).offset(skip).limit(limit)).all()


def update_product(
        db: Session, 
        product_id: int, 
        product_in: ProductUpdate,
        ) -> Optional[Product]:
    
    product = db.get(Product, product_id)
    if not product:
        return None
    
    for key, value in product.model_dump(exclude_unset=True).items():
        setattr(product, key, value)

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product_id: int) -> bool:

    product = db.get(Product, product_id)
    if product:
        db.delete(product)
        db.commit()
        return True
    
    return False
