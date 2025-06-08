from pydantic import BaseModel
from typing import List


class Coords(BaseModel):
    lat: float
    lng: float


class ShopCreate(BaseModel):
    name: str
    address: str
    coords: Coords
    ownerId: int


class ShopOut(BaseModel):
    id: int
    name: str
    address: str | None = None
    lat: float
    lng: float
    ownerId: int

    class Config:
        orm_mode = True


class ProductOut(BaseModel):
    id: int
    shopId: int
    name: str
    description: str | None = None
    price: float
    image_url: str | None = None

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None


class OrderItemIn(BaseModel):
    productId: int
    quantity: int


class OrderCreate(BaseModel):
    shopId: int
    items: List[OrderItemIn]
    pickupTime: str


class OrderStatusOut(BaseModel):
    id: int
    status: str
    payment_status: str | None = None
