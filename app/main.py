from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from .routers import users_router, products_router

app = FastAPI()

app.include_router(users_router)
app.include_router(products_router)