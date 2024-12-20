from typing import Optional
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

    class Config:
        orm_mode = True


class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True

