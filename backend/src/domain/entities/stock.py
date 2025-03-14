from pydantic import BaseModel
from typing import List
from src.domain.entities.beer import Beer

class Stock(BaseModel):
    last_updated: str
    beers: List[Beer]