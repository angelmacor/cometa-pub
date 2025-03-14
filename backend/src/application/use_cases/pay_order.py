from src.domain.repositories.order_repository import OrderRepository
from src.domain.exceptions import OrderNotFoundError, OrderAlreadyPaidError

class PayOrder:
    def __init__(self, order_repository):
        self.order_repository = order_repository

    def execute(self, order_id: str):
        order = self.order_repository.get_order_by_id(order_id)
        if not order:
            raise OrderNotFoundError(f"Order {order_id} not found")
        
        if order.paid:
            raise OrderAlreadyPaidError(f"Order {order_id} is already paid")

        order.paid = True
        self.order_repository.update_order(order)
        return order