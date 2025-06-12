import os
import shutil
from sqlalchemy.orm import Session

from .settings import get_settings
from .db import SessionLocal
from .models import Product

settings = get_settings()


def _local_remove_bg(input_path: str, output_path: str) -> None:
    """Placeholder for background removal using U\u00b2-Net or an API."""
    shutil.copy(input_path, output_path)


def remove_background(product_id: int, raw_path: str) -> None:
    processed_dir = os.path.join(settings.media_root, "products")
    os.makedirs(processed_dir, exist_ok=True)
    final_path = os.path.join(processed_dir, f"{product_id}.png")
    _local_remove_bg(raw_path, final_path)
    db: Session = SessionLocal()
    try:
        product = db.query(Product).get(product_id)
        if product:
            product.image = final_path
            db.commit()
    finally:
        db.close()
