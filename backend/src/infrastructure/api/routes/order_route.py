from fastapi import APIRouter, HTTPException
from typing import List
from src.application.use_cases.get_order_status import GetOrderStatus
from src.application.use_cases.calculate_order_total import CalculateOrderTotal
from src.application.use_cases.validate_stock import ValidateStock
from src.infrastructure.api.schemas.order_schema import OrderRequest, OrderResponse, OrderRoundResponse, OrderItemResponse
from src.infrastructure.repositories.order_repository import OrderRepository
from src.infrastructure.repositories.stock_repository import StockRepository
from src.domain.exceptions import (
    OrderNotFoundError, 
    OrderAlreadyPaidError, 
    BeerNotFoundError, 
    InsufficientStockError
)

router = APIRouter()

@router.get("/", response_model=OrderResponse)
def get_order():
    order_repository = OrderRepository()
    order = order_repository.get_order()
    return map_order_response(order)

@router.get("/pending", response_model=OrderResponse)
def get_pending_order():
    order_repository = OrderRepository()
    order = order_repository.get_pending_order()
    return map_order_response(order)

@router.post("/")
def add_order(order_request: OrderRequest):
    try:
        order_repository = OrderRepository()
        stock_repository = StockRepository()
        
        # Validate stock
        validate_stock = ValidateStock(stock_repository)
        beer = validate_stock.execute(order_request.name, order_request.quantity)
        
        # Process order
        order = order_repository.add_order(order_request, beer.price)
        beer.quantity -= order_request.quantity
        
        return order
        
    except BeerNotFoundError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except InsufficientStockError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/pay", response_model=OrderResponse)
def pay_current_order():
    try:
        order_repository = OrderRepository()
        paid_order = order_repository.mark_as_paid_last()
        if not paid_order:
            raise OrderNotFoundError("No order found to pay")
        return map_order_response(paid_order)
    except OrderNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except OrderAlreadyPaidError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/reset", response_model=OrderResponse)
def reset_orders():
    """Reset all orders and create a new empty one"""
    order_repository = OrderRepository()
    new_order = order_repository.reset_orders()
    return map_order_response(new_order)

def map_order_response(order) -> OrderResponse:
    """Map Order data to OrderResponse schema for frontend."""
    taxes = CalculateOrderTotal.add_taxes(order.subtotal)
    total = round(order.subtotal + taxes, 2)
    print(order)
    return OrderResponse(
        created=order.created,
        status="pending" if not order.paid else "paid",
        subtotal=round(order.subtotal, 2),
        taxes=taxes,
        total=CalculateOrderTotal.apply_total_discount(total),
        discounts=round(order.discounts, 2),
        rounds=[
            OrderRoundResponse(
                created=round.created,
                items=[
                    OrderItemResponse(
                        name=getattr(item, 'name', None),
                        quantity=getattr(item, 'quantity', 0),
                        price_per_unit=float(getattr(item, 'price_per_unit', 0)),
                        total_price=float(getattr(item, 'subtotal', 0)),
                        discounts=float(getattr(item, 'discounts', 0))
                    )
                    for item in round.items
                ]
            )
            for round in order.rounds
        ]
    )
