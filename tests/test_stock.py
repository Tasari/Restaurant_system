from tables.stock import Stock
from unittest.mock import MagicMock
from wallet import Wallet

def test_stock_creation():
    stock = Stock('eggs', 0.5)
    assert stock.name == 'Eggs'
    assert stock.quantity == 0
    assert stock.restock_price == 0.5

def test_restock_add():
    stock = Stock('ham', 1)
    stock.restock(15, Wallet(99999))
    assert stock.quantity == 15
    stock.restock(15, Wallet(99999))
    assert stock.quantity == 30
    assert stock.quantity != 15

def test_restock_set():
    stock = Stock('spam', 15)
    stock.restock(15, Wallet(99999), mode='set')
    assert stock.quantity == 15
    stock.restock(15, Wallet(99999), mode='set')
    assert stock.quantity == 15
    assert stock.quantity != 30