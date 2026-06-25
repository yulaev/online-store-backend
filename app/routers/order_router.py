from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.crud import add_to_cart
from app.schemas import AddToCartBody
from typing import Annotated
from app.utilities import oauth2_scheme

router = APIRouter(
    prefix="/order",
    tags=["order"]
)

@router.post("/add-to-cart")
async def add_to_cart_r(token: Annotated[str, Depends(oauth2_scheme)], item_data: AddToCartBody):
    add_to_cart(token, item_data)
    return JSONResponse(status_code=201, content={"message": "Succesfully added to cart"})
