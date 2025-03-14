import pytest
from datetime import datetime
from src.application.use_cases.validate_stock import ValidateStock
from src.domain.exceptions import BeerNotFoundError, InsufficientStockError
from src.domain.entities.stock import Stock
from src.domain.entities.beer import Beer

class TestValidateStock:
    @pytest.fixture
    def stock_repository_mock(self):
        class StockRepositoryMock:
            def get_stock(self):
                return Stock(
                    last_updated=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    beers=[
                        Beer(
                            nameID="existing-beer",
                            name="ExistingBeer",
                            quantity=5,
                            price=10.0
                        )
                    ]
                )
                
            def get_beer(self, name):
                if name == "NonExistentBeer":
                    return None
                return Beer(
                    nameID="existing-beer",
                    name="ExistingBeer",
                    quantity=5,
                    price=10.0
                )
        return StockRepositoryMock()

    @pytest.fixture
    def validate_stock(self, stock_repository_mock):
        return ValidateStock(stock_repository_mock)

    def test_execute_with_valid_beer_and_quantity(self, validate_stock):
        beer = validate_stock.execute("ExistingBeer", 3)
        assert beer.quantity == 5
        assert beer.price == 10.0

    def test_execute_with_non_existent_beer(self, validate_stock):
        with pytest.raises(BeerNotFoundError):
            validate_stock.execute("NonExistentBeer", 1)

    def test_execute_with_insufficient_stock(self, validate_stock):
        with pytest.raises(InsufficientStockError):
            validate_stock.execute("ExistingBeer", 6)