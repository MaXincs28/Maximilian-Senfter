from celery import Celery

from .settings import get_settings

settings = get_settings()

celery_app = Celery('backend', broker=settings.celery_broker_url)
