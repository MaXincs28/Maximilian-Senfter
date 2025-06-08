from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import stripe

from .db import get_db
from .models import Order, OrderItem, Product, Shop
from .auth import get_current_user
from .schemas import OrderCreate, OrderStatusOut
from .settings import get_settings

router = APIRouter(prefix="/orders", tags=["orders"])
settings = get_settings()
stripe.api_key = settings.stripe_api_key


@router.post("", response_model=dict)
def create_order(order_in: OrderCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    shop = db.query(Shop).filter(Shop.id == order_in.shopId).first()
    if not shop:
        raise HTTPException(status_code=404, detail="Shop not found")

    total = 0.0
    items: list[tuple[Product, int]] = []
    for item in order_in.items:
        product = db.query(Product).filter(Product.id == item.productId, Product.shop_id == order_in.shopId).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        items.append((product, item.quantity))
        total += float(product.price) * item.quantity

    order = Order(
        user_id=user["id"],
        shop_id=order_in.shopId,
        total_price=total,
        pickup_time=datetime.fromisoformat(order_in.pickupTime),
    )
    db.add(order)
    db.commit()
    db.refresh(order)

    for product, qty in items:
        db.add(OrderItem(order_id=order.id, product_id=product.id, quantity=qty))
    db.commit()

    intent = stripe.PaymentIntent.create(
        amount=int(total * 100),
        currency="usd",
        automatic_payment_methods={"enabled": True},
    )
    order.payment_intent_id = intent["id"]
    db.commit()

    return {"orderId": order.id, "paymentUrl": intent.client_secret}


@router.get("/{order_id}", response_model=OrderStatusOut)
def get_order(order_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    order = db.query(Order).filter(Order.id == order_id, Order.user_id == user["id"]).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    payment_status = None
    if order.payment_intent_id:
        intent = stripe.PaymentIntent.retrieve(order.payment_intent_id)
        payment_status = intent.status

    return OrderStatusOut(id=order.id, status=order.status, payment_status=payment_status)
