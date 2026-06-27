from pydantic import BaseModel, Field
from app.models import OrderStatus

class PublicOrder(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    status: OrderStatus

class AddToCartBody(BaseModel):
    id: int
    quantity: int = Field(default=1, ge=1)