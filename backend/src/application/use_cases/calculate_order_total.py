from datetime import datetime, timedelta
from src.domain.entities.order import Order
from src.config.settings import settings

class CalculateOrderTotal:

    @staticmethod
    def apply_happy_hour(quantity: int) -> int:
        """Apply 'Buy 3, Get 1 Free' Happy Hour discount."""
        free_beers = quantity // settings.DISCOUNT_THRESHOLD  
        return free_beers
    
    @staticmethod
    def apply_weekend_discount(self, quantity: int) -> int:
        """Apply 'Buy 2, Get 1 Free' Weekend discount only on weekends."""
        current_day = datetime.now().weekday()
        if current_day >= 5:  # 5 is Saturday, 6 is Sunday
            free_beers = quantity // settings.DISCOUNT_WEEKEND_THRESHOLD
            self._order.discounts += free_beers
            return free_beers
        return 0
    
    @staticmethod
    def apply_total_discount(total: float) -> float:
        """Apply 15% discount when total is over 100."""
        if total > 100:
            totalWithDiscount = round(total-(total * 0.15), 2)
            return totalWithDiscount
        return total
    
    @staticmethod
    def add_taxes(subtotal: float) -> float:
        return round(subtotal * settings.TAX_RATE, 2)