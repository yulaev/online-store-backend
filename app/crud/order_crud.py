from app.database import get_session
from app.models import Product, User, Order, OrderItem, OrderStatus
from app.schemas import AddToCartBody
from app.utilities import oauth2_scheme, validate_token
from fastapi import Depends, HTTPException
from typing import Annotated
from sqlalchemy import select

def add_to_cart(token: Annotated[str, Depends(oauth2_scheme)], item_data: AddToCartBody):
    with get_session() as session:
        payload = validate_token(token)
        if payload.get("role") != "customer":
            raise HTTPException(status_code=403, detail="You are forbidden from performing this operation")
        
        u_stmt = select(User).where(User.name == payload.get("sub"))
        user = session.scalar(u_stmt)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        p_stmt = select(Product).where(Product.id == item_data.id)
        product = session.scalar(p_stmt)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        
        if item_data.quantity > product.quantity:
            raise HTTPException(status_code=400, detail="Quantity exceeds available")

        o_stmt = select(Order).where(Order.customer_id == user.id)
        order = session.scalar(o_stmt)
        if not order:
            order = Order (
                customer_id = user.id
            )

            session.add(order)
            session.commit()
        
        order_item = OrderItem (
            order_id = order.id,
            product_id = product.id,
            quantity = item_data.quantity,
            status = OrderStatus.pending
        )

        session.add(order_item)
        session.commit()