from datetime import datetime
from src.domain.entities.stock import Stock
from src.domain.entities.beer import Beer
from src.application.ports.repositories import StockRepositoryPort


class StockRepository(StockRepositoryPort):
    _stock = Stock(
        last_updated=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        beers=[
            Beer(nameID="CometaIPA", name="Cometa IPA", price=5.35, quantity=110),
            Beer(nameID="CometaAPA", name="Cometa Apa", price=4.75, quantity=30),
            Beer(nameID="CometaLager", name="Cometa Lager", price=4.25, quantity=4)
        ]
    )

    def get_stock(self) -> Stock:
        return self._stock
