from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
from geoalchemy2 import WKTElement

from .db import get_db
from .models import Shop
from .auth import get_current_user
from .schemas import ShopCreate, ShopOut

router = APIRouter(prefix="/shops", tags=["shops"])


@router.post("", response_model=ShopOut)
def create_shop(shop_in: ShopCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    point = WKTElement(f"POINT({shop_in.coords.lng} {shop_in.coords.lat})", srid=4326)
    shop = Shop(name=shop_in.name, address=shop_in.address, owner_id=shop_in.ownerId, location=point)
    db.add(shop)
    db.commit()
    db.refresh(shop)
    return ShopOut(
        id=shop.id,
        name=shop.name,
        address=shop.address,
        lat=shop_in.coords.lat,
        lng=shop_in.coords.lng,
        ownerId=shop.owner_id,
    )


@router.get("", response_model=list[ShopOut])
def list_shops(
    lat: float | None = Query(None),
    lng: float | None = Query(None),
    radius: float | None = Query(None),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    query = db.query(
        Shop.id,
        Shop.name,
        Shop.address,
        func.ST_Y(Shop.location).label("lat"),
        func.ST_X(Shop.location).label("lng"),
        Shop.owner_id.label("ownerId"),
    )
    if lat is not None and lng is not None and radius is not None:
        point = WKTElement(f"POINT({lng} {lat})", srid=4326)
        query = query.filter(func.ST_DWithin(Shop.location, point, radius))
    rows = query.all()
    return [ShopOut(**row._asdict()) for row in rows]


@router.get("/{shop_id}", response_model=ShopOut)
def get_shop(shop_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    row = db.query(
        Shop.id,
        Shop.name,
        Shop.address,
        func.ST_Y(Shop.location).label("lat"),
        func.ST_X(Shop.location).label("lng"),
        Shop.owner_id.label("ownerId"),
    ).filter(Shop.id == shop_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Shop not found")
    return ShopOut(**row._asdict())
