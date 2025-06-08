from fastapi import FastAPI, Depends, HTTPException, Header
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


def get_current_user(authorization: str | None = Header(None)):
    if not authorization or not authorization.startswith('Bearer '):
        raise HTTPException(status_code=401, detail='Invalid auth header')
    token = authorization.split(' ')[1]
    username = auth.decode_access_token(token)
    if not username:
        raise HTTPException(status_code=401, detail='Invalid token')
    return username

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


@app.post('/shops')
def create_shop(shop: schemas.ShopCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    owner = db.query(models.ShopOwner).filter_by(username=current_user).first()
    if not owner:
        raise HTTPException(status_code=404, detail='Owner not found')
    db_shop = models.Shop(name=shop.name, owner_id=owner.id)
    db.add(db_shop)
    db.commit()
    db.refresh(db_shop)
    return {"id": db_shop.id, "name": db_shop.name}


@app.post('/products')
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    shop = db.query(models.Shop).filter_by(id=product.shop_id).first()
    if not shop:
        raise HTTPException(status_code=404, detail='Shop not found')
    owner = db.query(models.ShopOwner).filter_by(username=current_user).first()
    if shop.owner_id != owner.id:
        raise HTTPException(status_code=403, detail='Not owner of shop')
    db_product = models.Product(name=product.name, price=product.price, shop_id=product.shop_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return {"id": db_product.id, "name": db_product.name, "price": db_product.price}
