from fastapi import FastAPI
import uvicorn

if __name__ == "__main__" and __package__ is None:
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from backend.settings import get_settings
from backend.auth import router as auth_router
from backend.shops import router as shops_router
from backend.products import router as products_router
from backend.orders import router as orders_router

app = FastAPI()
settings = get_settings()

app.include_router(auth_router)
app.include_router(shops_router)
app.include_router(products_router)
app.include_router(orders_router)

@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
