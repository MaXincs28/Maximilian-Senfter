from fastapi import FastAPI
import uvicorn

from .settings import get_settings
from .auth import router as auth_router
from .shops import router as shops_router
from .products import router as products_router
from .orders import router as orders_router

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
