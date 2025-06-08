from pydantic import BaseModel

class ShopOwnerCreate(BaseModel):
    username: str
    password: str

class ShopOwnerLogin(BaseModel):
    username: str
    password: str
