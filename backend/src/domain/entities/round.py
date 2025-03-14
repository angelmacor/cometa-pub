from pydantic import BaseModel
from typing import List, Dict, Union
from .order_item import OrderItem

class Round(BaseModel):
    created: str
    items: List[OrderItem]