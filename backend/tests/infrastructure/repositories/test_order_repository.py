import pytest
from datetime import datetime
from src.infrastructure.repositories.order_repository import OrderRepository
from src.domain.entities.order import Order
from src.domain.entities.round import Round
from src.domain.entities.round_item import RoundItem

class TestOrderRepository:
    @pytest.fixture
    def order_repository(self):
        return OrderRepository()

    def test_get_order_returns_empty_order(self, order_repository):
        order = order_repository.get_order()
        assert order.paid == False
        assert order.subtotal == 0
        assert order.discounts == 0
        assert order.rounds == []

    def test_add_order_without_discount(self, order_repository):
        order_repository.reset_orders()
        order_request = type('OrderRequest', (), {'name': 'Beer1', 'quantity': 2})
        price_per_unit = 5.0
        
        result = order_repository.add_order(order_request, price_per_unit)
        assert float(result["subtotal"]) == 10.0

    def test_add_order_with_happy_hour_discount(self, order_repository):
        order_repository.reset_orders()
        order_request = type('OrderRequest', (), {'name': 'Beer1', 'quantity': 3})
        price_per_unit = 5.0
        result = order_repository.add_order(order_request, price_per_unit)
        assert float(result["subtotal"]) == 10.0  # 2 beers paid, 1 free
        assert float(result["discounts"]) == 5.0  # 1 free beer

    def test_mark_as_paid_last(self, order_repository):
        # Add an order first
        order_request = type('OrderRequest', (), {'name': 'Beer1', 'quantity': 2})
        order_repository.add_order(order_request, 5.0)

        # Mark it as paid
        paid_order = order_repository.mark_as_paid_last()

        assert paid_order.paid == True

    def test_reset_orders(self, order_repository):
        # Add an order first
        order_request = type('OrderRequest', (), {'name': 'Beer1', 'quantity': 2})
        order_repository.add_order(order_request, 5.0)

        # Reset orders
        new_order = order_repository.reset_orders()

        assert new_order.paid == False
        assert new_order.subtotal == 0
        assert new_order.discounts == 0
        assert len(new_order.rounds) == 0