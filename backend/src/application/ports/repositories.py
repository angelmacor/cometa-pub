from abc import ABC, abstractmethod
from src.domain.entities.order import Order
from src.domain.entities.stock import Stock

class OrderRepositoryPort(ABC):
    @abstractmethod
    def get_order(self) -> Order:
        pass

class StockRepositoryPort(ABC):
    @abstractmethod
    def get_stock(self) -> Stock:
        pass
