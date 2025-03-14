from src.application.ports.repositories import OrderRepositoryPort

class GetOrderStatus:
    def __init__(self, repository: OrderRepositoryPort):
        self.repository = repository

    def execute(self):
        order = self.repository.get_order()
        return order
