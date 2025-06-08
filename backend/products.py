from fastapi import APIRouter, Depends, HTTPException, File, UploadFile, Form
from sqlalchemy.orm import Session
import os
from uuid import uuid4

from .db import get_db
from .models import Product, Shop
from .auth import get_current_user
from .schemas import ProductOut, ProductUpdate
from .settings import get_settings
from .tasks import process_product_image

router = APIRouter(tags=["products"])
settings = get_settings()


@router.post("/shops/{shop_id}/products", response_model=ProductOut)
async def create_product(
    shop_id: int,
    name: str = Form(...),
    description: str | None = Form(None),
    price: float = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    if db.query(Shop).filter(Shop.id == shop_id).first() is None:
        raise HTTPException(status_code=404, detail="Shop not found")
    raw_dir = os.path.join(settings.media_root, "raw")
    os.makedirs(raw_dir, exist_ok=True)
    ext = os.path.splitext(image.filename)[1] or ".png"
    raw_path = os.path.join(raw_dir, f"{uuid4().hex}{ext}")
    with open(raw_path, "wb") as f:
        f.write(await image.read())

    product = Product(shop_id=shop_id, name=name, description=description, price=price)
    db.add(product)
    db.commit()
    db.refresh(product)

    process_product_image.delay(product.id, raw_path)

    return ProductOut(
        id=product.id,
        shopId=product.shop_id,
        name=product.name,
        description=product.description,
        price=float(product.price),
        image_url=None,
    )


@router.put("/products/{product_id}", response_model=ProductOut)
def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if payload.name is not None:
        product.name = payload.name
    if payload.description is not None:
        product.description = payload.description
    if payload.price is not None:
        product.price = payload.price
    db.commit()
    db.refresh(product)
    return ProductOut(
        id=product.id,
        shopId=product.shop_id,
        name=product.name,
        description=product.description,
        price=float(product.price),
        image_url=product.image,
    )


@router.delete("/products/{product_id}", status_code=204)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return None
