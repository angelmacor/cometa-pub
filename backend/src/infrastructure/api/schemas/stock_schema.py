from pydantic import BaseModel
class BeerResponse(BaseModel):
    nameId: str
    name: str
    price: float
    quantity: int
