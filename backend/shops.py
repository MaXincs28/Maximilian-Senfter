from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .db import get_db
from .models import Shop
from .auth import get_current_user
from .schemas import ShopCreate, ShopOut
import math

router = APIRouter(prefix="/shops", tags=["shops"])


@router.post("", response_model=ShopOut)
def create_shop(shop_in: ShopCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    shop = Shop(
        name=shop_in.name,
        address=shop_in.address,
        owner_id=shop_in.ownerId,
        lat=shop_in.coords.lat,
        lng=shop_in.coords.lng,
    )
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


@router.get("")
def list_shops(
    lat: float | None = Query(None),
    lng: float | None = Query(None),
    radius: float | None = Query(None),
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    """Return shops optionally filtered by distance from the given point."""
    query = db.query(Shop)
    shops = query.all()
    results = []
    for s in shops:
        if lat is not None and lng is not None and radius is not None:
            d = _distance(lat, lng, float(s.lat), float(s.lng))
            if d > radius:
                continue
        results.append(
            {
                "id": s.id,
                "name": s.name,
                "address": s.address,
                "latitude": float(s.lat),
                "longitude": float(s.lng),
            }
        )
    return results


@router.get("/{shop_id}", response_model=ShopOut)
def get_shop(shop_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    shop = db.query(Shop).filter(Shop.id == shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")
    return ShopOut(
        id=shop.id,
        name=shop.name,
        address=shop.address,
        lat=float(shop.lat),
        lng=float(shop.lng),
        ownerId=shop.owner_id,
    )


def _distance(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """Return distance in meters between two lat/lng points."""
    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lng2 - lng1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c
