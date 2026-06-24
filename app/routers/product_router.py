from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse


from typing import Annotated
from app.utilities import oauth2_scheme

router = APIRouter(
    prefix="/products",
    tags=["products"]
)