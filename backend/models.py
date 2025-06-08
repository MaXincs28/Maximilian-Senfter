from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from .db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    is_active = Column(Boolean, server_default='true', nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    shops = relationship('Shop', back_populates='owner')
    orders = relationship('Order', back_populates='user')


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    location = Column(Geometry('POINT'))

    owner = relationship('User', back_populates='shops')
    products = relationship('Product', back_populates='shop')


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    shop_id = Column(Integer, ForeignKey('shops.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Numeric(10, 2), nullable=False)

    shop = relationship('Shop', back_populates='products')
    orders = relationship('Order', back_populates='product')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    total_price = Column(Numeric(10, 2), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship('User', back_populates='orders')
    product = relationship('Product', back_populates='orders')
