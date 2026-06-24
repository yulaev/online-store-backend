from pydantic import BaseModel
from decimal import Decimal

class ProductCreate(BaseModel):
    name: str
    description: str
    price: Decimal
    quantity: int = 1

class ProductEdit(BaseModel):
    name: str | None = None
    description: str | None = None
    price: Decimal | None = None
    quantity: int | None = None