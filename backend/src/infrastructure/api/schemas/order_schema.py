from pydantic import BaseModel
from typing import List

class OrderItemResponse(BaseModel):
    name: str
    quantity: int
    price_per_unit: float
    total_price: float
    discounts: float

class OrderRoundResponse(BaseModel):
    created: str
    items: List[OrderItemResponse]

class OrderResponse(BaseModel):
    created: str
    status: str
    subtotal: float
    taxes: float
    total: float
    discounts: float
    rounds: List[OrderRoundResponse]

class OrderRequest(BaseModel):
    name: str
    quantity: int
