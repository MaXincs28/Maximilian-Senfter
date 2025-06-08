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
    address = Column(String)
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
    image = Column(String)

    shop = relationship('Shop', back_populates='products')
    order_items = relationship('OrderItem', back_populates='product')


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    shop_id = Column(Integer, ForeignKey('shops.id'), nullable=False)
    total_price = Column(Numeric(10, 2), nullable=False)
    pickup_time = Column(DateTime(timezone=True), nullable=False)
    status = Column(String, nullable=False, server_default='pending')
    payment_intent_id = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship('User', back_populates='orders')
    shop = relationship('Shop')
    items = relationship('OrderItem', back_populates='order')


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    order = relationship('Order', back_populates='items')
    product = relationship('Product')
