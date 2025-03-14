import pytest
from src.application.use_cases.calculate_order_total import CalculateOrderTotal

class TestCalculateOrderTotal:
    def test_apply_happy_hour_with_three_beers(self):
        free_beers = CalculateOrderTotal.apply_happy_hour(3)
        assert free_beers == 1

    def test_apply_happy_hour_with_two_beers(self):
        free_beers = CalculateOrderTotal.apply_happy_hour(2)
        assert free_beers == 0

    def test_add_taxes(self):
        taxes = CalculateOrderTotal.add_taxes(100)
        assert taxes == 15.0  # 15% tax rate

    def test_apply_total_discount(self):
        total_with_discount = CalculateOrderTotal.apply_total_discount(200)
        assert total_with_discount == 170.0  # 15% discount for orders over 100