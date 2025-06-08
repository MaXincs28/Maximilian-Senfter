from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, auth, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/register')
def register(shop_owner: schemas.ShopOwnerCreate, db: Session = Depends(get_db)):
    existing = db.query(models.ShopOwner).filter_by(username=shop_owner.username).first()
    if existing:
        raise HTTPException(status_code=400, detail='Username already registered')
    hashed = auth.get_password_hash(shop_owner.password)
    db_shop_owner = models.ShopOwner(username=shop_owner.username, password_hash=hashed)
    db.add(db_shop_owner)
    db.commit()
    db.refresh(db_shop_owner)
    return {"id": db_shop_owner.id, "username": db_shop_owner.username}

@app.post('/login')
def login(shop_owner: schemas.ShopOwnerLogin, db: Session = Depends(get_db)):
    db_owner = db.query(models.ShopOwner).filter_by(username=shop_owner.username).first()
    if not db_owner or not auth.verify_password(shop_owner.password, db_owner.password_hash):
        raise HTTPException(status_code=400, detail='Incorrect username or password')
    token = auth.create_access_token({"sub": db_owner.username})
    return {"access_token": token, "token_type": "bearer"}
