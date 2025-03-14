from fastapi import FastAPI
from src.infrastructure.api.routes import stock_route, order_route

app = FastAPI()

app.include_router(stock_route.router, prefix="/stock")
app.include_router(order_route.router, prefix="/order")