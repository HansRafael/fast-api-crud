from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
#from utils.auth import create_access_token
from models.user import User
from module import product_module
from schemas.product_schema import ProductCreate, ProductResponse, ProductUpdate
from database import SessionLocal, get_db
from models.product import Product
from utils import auth

router = APIRouter()


""" With more time, I would split this into a different way 
    Controller -> UserCase -> Call the necessary Modules -> Repositories
"""
@router.get("/products", tags=["Products"])
def get_products(db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return product_module.get_all_products(db)

@router.post("/products", tags=["Products"])
def create_product(product: ProductCreate, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return product_module.create_new_product(db, product)

@router.delete("/products/{product_id}", tags=["Products"])
def delete_product(product_id: int, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return product_module.delete_product_by_id(db, product_id)

@router.put("/products/{product_id}", tags=["Products"])
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db), current_user: User = Depends(auth.get_current_user)):
    return product_module.update_product_by_id(db, product_id, product)