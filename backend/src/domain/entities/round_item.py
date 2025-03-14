from pydantic import BaseModel

class RoundItem(BaseModel):
    name: str
    quantity: int
    price: float = 0