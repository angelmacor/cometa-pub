from datetime import datetime
from src.domain.entities.stock import Stock
from src.domain.entities.beer import Beer

class InMemoryStockRepository:
    def __init__(self):
        self.beers = [
            Beer(nameID="corona", name="Corona", quantity=10, price=115),
            Beer(nameID="club-colombia", name="Club Colombia", quantity=15, price=110)
        ]

    def get_stock(self):
        return Stock(
            last_updated=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            beers=self.beers
        )

    def get_beer(self, name: str) -> Beer:
        return next((beer for beer in self.beers if beer.name == name), None)