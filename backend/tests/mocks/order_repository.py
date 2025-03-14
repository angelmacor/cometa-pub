from datetime import datetime
from src.domain.entities.order import Order
from src.domain.entities.round import Round
from src.domain.entities.order_item import OrderItem

class InMemoryOrderRepository:
    def __init__(self):
        self._order = Order(
            created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            paid=False,
            subtotal=0,
            taxes=0,
            discounts=0,
            total=0,
            items=[],
            rounds=[]
        )

    def get_order(self):
        return self._order

    def add_order(self, order_request, price_per_unit):
        quantity = order_request.quantity
        new_round = Round(
            created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            items=[
                OrderItem(
                    name=order_request.name,
                    quantity=quantity,
                    price_per_unit=price_per_unit
                )
            ]
        )
        self._order.rounds.append(new_round)
        self._order.subtotal += price_per_unit * quantity
        self._order.taxes = self._order.subtotal * 0.19
        self._order.discounts = self._order.subtotal * 0.10
        return self._order

    def mark_as_paid(self):
        self._order.paid = True
        return self._order