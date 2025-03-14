from pydantic import BaseModel
from typing import List
from src.domain.entities.order_item import OrderItem
from src.domain.entities.round import Round

class Order(BaseModel):
    created: str
    paid: bool
    subtotal: float
    taxes: float
    discounts: float
    items: List[OrderItem]
    rounds: List[Round]