import pytest
from datetime import datetime
from fastapi import HTTPException
from src.application.use_cases.order_management import OrderManagement
from src.domain.exceptions import BeerNotFoundError, InsufficientStockError
from tests.mocks.stock_repository import InMemoryStockRepository
from src.domain.entities.order import Order
from src.domain.entities.round import Round
from src.domain.entities.order_item import OrderItem  # Add this import
from tests.mocks.order_repository import InMemoryOrderRepository


@pytest.fixture
def order_management_use_case():
    stock_repository = InMemoryStockRepository()
    order_repository = InMemoryOrderRepository()
    return OrderManagement(stock_repository, order_repository)

def test_get_empty_order(order_management_use_case):
    order = order_management_use_case.get_order()
    assert order.paid == False
    assert order.subtotal == 0
    assert order.taxes == 0
    assert order.discounts == 0
    assert len(order.items) == 0
    assert len(order.rounds) == 0

def test_add_valid_round(order_management_use_case):
    round = Round(
        created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        items=[
            OrderItem(name="Corona", quantity=4, price_per_unit=5.5),
        ]
    )
    
    order = order_management_use_case.add_round(round)
    assert len(round.items) == 1
    assert order.subtotal == 460 
    assert order.taxes == pytest.approx(460*0.19)  # 19% of 460
    assert order.discounts == pytest.approx(460*0.1)  # Below 500 threshold

def test_add_round_with_discount(order_management_use_case):
    round = Round(
        created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        items=[OrderItem(name="Corona", quantity=3, price_per_unit=115)]
    )
    
    order = order_management_use_case.add_round(round)
    
    total = (115 * 3) 
    assert order.subtotal == total
    assert order.taxes == pytest.approx(total * 0.19)
    assert order.discounts == pytest.approx(total * 0.1)  # 10% discount

def test_insufficient_stock(order_management_use_case):
    # Set up a round with quantity higher than available stock
    round = Round(
        created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        items=[
            OrderItem(name="Corona", quantity=10000, price_per_unit=5.5),
        ]
    )
    
    with pytest.raises(HTTPException) as exc_info:
        order_management_use_case.add_round(round)
    
    assert exc_info.value.status_code == 400
    assert "Insufficient stock" in str(exc_info.value.detail)

def test_beer_not_found(order_management_use_case):
    round = Round(
        created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        items=[
            OrderItem(name="Invalid Beer", quantity=4, price_per_unit=5.5),
        ]
    )
    
    with pytest.raises(HTTPException) as exc_info:
        order_management_use_case.add_round(round)
    
    assert exc_info.value.status_code == 404
    assert "Beer Invalid Beer not found" in str(exc_info.value.detail)


def test_validate_order_success(order_management_use_case):
    beer = order_management_use_case.validate_order("Corona", 2)
    assert beer.name == "Corona"  # Changed from dict access to object attribute
    assert beer.quantity >= 2

def test_validate_order_insufficient_stock(order_management_use_case):
    with pytest.raises(InsufficientStockError):
        order_management_use_case.validate_order("Corona", 1000)