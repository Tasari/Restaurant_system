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

def test_restock_add_wallet():
    stock = Stock('ham', 1)
    wallet = Wallet(50)
    stock.restock(15, wallet)
    assert wallet.money == 35
    stock.restock(15, wallet)
    assert wallet.money == 20

def test_restock_set_wallet():
    stock = Stock('spam', 15)
    wallet = Wallet(250)
    stock.restock(15, wallet, mode='set')
    assert wallet.money == 25
    stock.restock(15, wallet, mode='set')
    assert wallet.money == 25
    stock.restock(10, wallet, mode='set')
    assert wallet.money == 100