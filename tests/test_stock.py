from tables.stock import Stock
from unittest.mock import MagicMock

def test_stock_creation():
    stock = Stock('eggs', 0.5)
    assert stock.name == 'eggs'
    assert stock.quantity == 0
    assert stock.restock_price == 0.5

def test_restock_add():
    stock = Stock('ham', 1)
    stock.restock(15)
    assert stock.quantity == 15
    stock.restock(15)
    assert stock.quantity == 30
    assert stock.quantity != 15

def test_restock_set():
    stock = Stock('spam', 15)
    stock.restock(15, mode='set')
    assert stock.quantity == 15
    stock.restock(15, mode='set')
    assert stock.quantity == 15
    assert stock.quantity != 30