import uvicorn
from fastapi import FastAPI
from .infrastructure.api.middleware import setup_cors
from .infrastructure.api.routes import order_router, stock_router
from .config.settings import settings

# Init FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG
)

setup_cors(app)


# Routes
app.include_router(order_router, prefix="/order", tags=["Order"])
app.include_router(stock_router, prefix="/stock", tags=["Stock"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
