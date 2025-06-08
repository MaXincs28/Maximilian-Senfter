from pydantic import BaseModel

class ShopOwnerCreate(BaseModel):
    username: str
    password: str

class ShopOwnerLogin(BaseModel):
    username: str
    password: str


class ShopCreate(BaseModel):
    name: str


class ProductCreate(BaseModel):
    name: str
    price: float
    shop_id: int
