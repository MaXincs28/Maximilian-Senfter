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
