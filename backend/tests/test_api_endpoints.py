from fastapi.testclient import TestClient
from src.main import app  # Update this import to match your main app location
from src.domain.entities.order import Order
from src.domain.entities.round import Round
from src.domain.entities.round_item import RoundItem

client = TestClient(app)

def test_get_stock():
    response = client.get("/stock")
    assert response.status_code == 200
    data = response.json()
    assert "beers" in data

def test_get_beers():
    response = client.get("/stock/beers")
    assert response.status_code == 200
    beers = response.json()
    assert isinstance(beers, list)
    for beer in beers:
        assert "name" in beer
        assert "price" in beer
        assert "quantity" in beer

def test_get_orders():
    response = client.get("/order")
    assert response.status_code == 200
    orders = response.json()
    assert isinstance(orders, dict)  # Changed to dict since we return a single order

def test_add_valid_order():
    # Reset orders first
    client.post("/order/reset")
    
    response = client.post("/order", json={
        "name": "Cometa IPA",
        "quantity": 2
    }) 
    
    assert response.status_code == 200
    data = response.json()
    assert "subtotal" in data
    assert "discounts" in data
    assert "rounds" in data

def test_add_order_invalid_beer():
    order_data = {
        "name": "Invalid Beer",
        "quantity": 1
    }
    order_request = type('OrderRequest', (), order_data)
    response = client.post("/order", json=order_data)
    assert response.status_code == 400
    assert "detail" in response.json()

def test_add_order_insufficient_stock():
    order_data = {
        "name": "Corona",
        "quantity": 1000
    }
    response = client.post("/order", json=order_data)
    assert response.status_code == 400
    assert "detail" in response.json()

def test_pay_order():
    # Reset orders first
    client.post("/order/reset")

    # Add an order first to have something to pay
    add_response = client.post("/order", json={
        "name": "Cometa IPA",
        "quantity": 2
    })
    assert add_response.status_code == 200
    
    # Pay the order
    pay_response = client.post("/order/pay")
    assert pay_response.status_code == 200
    data = pay_response.json()
    
    # Verify order status
    assert isinstance(data, dict)
    assert "status" in data
    assert data["status"] == "paid"
    assert "rounds" in data

def test_reset_orders():
    response = client.post("/order/reset")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "pending"
    assert data["subtotal"] == 0