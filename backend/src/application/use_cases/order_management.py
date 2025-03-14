from datetime import datetime
from fastapi import HTTPException
from src.domain.exceptions import BeerNotFoundError, InsufficientStockError

class OrderManagement:
    def __init__(self, stock_repository, order_repository):
        self.stock_repository = stock_repository
        self.order_repository = order_repository

    def get_order(self):
        return self.order_repository.get_order()

    def add_round(self, round):
        try:
            # Validate all items before processing
            for item in round.items:
                self.validate_order(item.name, item.quantity)
            
            # Process the first item (current implementation limitation)
            item = round.items[0]
            beer = self.stock_repository.get_beer(item.name)
            order_request = type('OrderRequest', (), {
                'name': item.name,
                'quantity': item.quantity
            })
            
            return self.order_repository.add_order(order_request, beer.price)
            
        except (BeerNotFoundError, InsufficientStockError) as e:
            if isinstance(e, BeerNotFoundError):
                raise HTTPException(status_code=404, detail=str(e))
            raise HTTPException(status_code=400, detail=str(e))

    def validate_order(self, name: str, quantity: int):
        beer = self.stock_repository.get_beer(name)
        if not beer:
            raise BeerNotFoundError(f"Beer {name} not found")
        if beer.quantity < quantity:
            raise InsufficientStockError(f"Insufficient stock for {name}. Available: {beer.quantity}")
        return beer
