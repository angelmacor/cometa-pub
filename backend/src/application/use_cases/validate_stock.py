from src.domain.exceptions import BeerNotFoundError, InsufficientStockError

class ValidateStock:
    def __init__(self, stock_repository):
        self.stock_repository = stock_repository

    def execute(self, beer_name: str, quantity: int):
        stock = self.stock_repository.get_stock()
        beer = next((b for b in stock.beers if b.name == beer_name), None)
        
        if not beer:
            raise BeerNotFoundError(f"Beer {beer_name} not found")
            
        if beer.quantity < quantity:
            raise InsufficientStockError(f"Only {beer.quantity} {beer_name} available in stock")
            
        return beer