from pydantic import BaseModel

class OrderItem(BaseModel):
    name: str
    price_per_unit: float = 0
    quantity: int
    subtotal: float = 0
    discounts: float = 0 
    total: float = 0

