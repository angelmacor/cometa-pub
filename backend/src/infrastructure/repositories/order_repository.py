from datetime import datetime
from src.domain.entities.order import Order
from src.domain.entities.round import Round
from src.application.ports.repositories import OrderRepositoryPort
from src.application.use_cases.calculate_order_total import CalculateOrderTotal

from src.config.settings import settings

from typing import List, Dict, Union


class OrderRepository(OrderRepositoryPort):
    _order = Order(
        created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        paid=False,
        subtotal=0,
        taxes=0,
        discounts=0,
        total=0,
        items=[],
        rounds=[]
    )

    def get_order(self) -> Order:
        return self._order
    
    def get_pending_order(self) -> Order:
        if not self._order.paid:
            return self._order
        return None
    
    def add_order(self, orderRequest: {str,int}, price_per_unit: float) -> Order:
        """ Adds a new order round to the existing order """

        quantity = orderRequest.quantity
        freeBeer = CalculateOrderTotal.apply_happy_hour(quantity)
        subtotal = price_per_unit * (quantity - freeBeer)
        discounts = freeBeer * price_per_unit
        total = subtotal + CalculateOrderTotal.add_taxes(subtotal)

        new_round = Round(
            created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            items=[{
                    "name": orderRequest.name, 
                    "quantity": quantity, 
                    "price_per_unit": f"{price_per_unit:.2f}",
                    "subtotal": f"{subtotal:.2f}",
                    "discounts": f"{discounts:.2f}",
                    "total": f"{total:.2f}"
                    }]
        )
        
        self._order.rounds.append(new_round)
        self._order.subtotal += subtotal
        self._order.discounts += discounts

        return {
                "subtotal": f"{self._order.subtotal:.2f}",
                "discounts": f"{self._order.discounts:.2f}",
                "rounds": self._order.rounds
            }
    
    def mark_as_paid_last(self) -> Order:
        """Marks the last order as paid and creates a new empty order"""
        if self._order:
            self._order.paid = True
            return self._order
        return None
    
    def reset_orders(self) -> Order:
        """Reset all order and create a new empty one"""
        OrderRepository._order = Order(
            created=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            paid=False,
            subtotal=0,
            taxes=0,
            discounts=0,
            total=0,
            items=[],
            rounds=[]
        )
        
        return OrderRepository._order
