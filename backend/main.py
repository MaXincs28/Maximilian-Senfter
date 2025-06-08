from fastapi import FastAPI
import uvicorn
from .settings import get_settings
from .db import get_db

app = FastAPI()
settings = get_settings()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
