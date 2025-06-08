from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session

from .settings import get_settings
from .db import get_db
from .models import Product
from .auth import router as auth_router, get_current_user
from .shops import router as shops_router

app = FastAPI()
settings = get_settings()

app.include_router(auth_router)
app.include_router(shops_router)


@app.get("/products")
def list_products(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return db.query(Product).all()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
