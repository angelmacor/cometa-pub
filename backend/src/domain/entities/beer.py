from pydantic import BaseModel

class Beer(BaseModel):
    nameID: str
    name: str
    price: float
    quantity: int