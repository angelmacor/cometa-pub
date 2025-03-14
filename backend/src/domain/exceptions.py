class OrderNotFoundError(Exception):
    pass

class OrderAlreadyPaidError(Exception):
    pass

class BeerNotFoundError(Exception):
    pass

class InsufficientStockError(Exception):
    pass