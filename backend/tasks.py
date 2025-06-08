from celery import Celery
from sqlalchemy.orm import Session
import shutil
import os

from .settings import get_settings
from .db import SessionLocal, engine
from .models import Product

settings = get_settings()

celery_app = Celery('tasks', broker=settings.celery_broker_url)


def remove_bg(input_path: str, output_path: str):
    """Placeholder for background removal."""
    shutil.copy(input_path, output_path)


@celery_app.task
def process_product_image(product_id: int, raw_path: str):
    processed_dir = os.path.join(settings.media_root, "products")
    os.makedirs(processed_dir, exist_ok=True)
    final_path = os.path.join(processed_dir, f"{product_id}.png")
    remove_bg(raw_path, final_path)
    db: Session = SessionLocal()
    try:
        product = db.query(Product).get(product_id)
        if product:
            product.image = final_path
            db.commit()
    finally:
        db.close()
