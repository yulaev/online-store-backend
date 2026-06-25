from pydantic import BaseModel, Field

class AddToCartBody(BaseModel):
    id: int
    quantity: int = Field(default=1, ge=1)