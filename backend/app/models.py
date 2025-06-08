from sqlalchemy import Column, Integer, String
from .database import Base

class ShopOwner(Base):
    __tablename__ = 'shop_owners'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
