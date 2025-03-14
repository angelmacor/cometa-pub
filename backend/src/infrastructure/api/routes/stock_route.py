from fastapi import APIRouter
from src.application.use_cases.get_stock_status import GetStockStatus
from src.domain.entities.stock import Stock
from src.infrastructure.repositories.stock_repository import StockRepository
from src.infrastructure.api.schemas.stock_schema import BeerResponse
from typing import List


router = APIRouter()

@router.get("/", response_model=Stock)
def get_stock():
    repository = StockRepository()
    use_case = GetStockStatus(repository)
    return use_case.execute()


@router.get("/beers", response_model=List[BeerResponse])
def get_beers():
    repository = StockRepository()
    stock = repository.get_stock()
    return [
        BeerResponse(
            nameId=beer.nameID,
            name=beer.name,
            price=beer.price,
            quantity=beer.quantity
        ) 
        for beer in stock.beers
    ]