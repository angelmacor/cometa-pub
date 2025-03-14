from src.application.ports.repositories import StockRepositoryPort

class GetStockStatus:
    def __init__(self, repository: StockRepositoryPort):
        self.repository = repository

    def execute(self):
        order = self.repository.get_stock()
        return order
