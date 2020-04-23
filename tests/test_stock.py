from tables.stock import Stock
from wallet import Wallet
from tools import string_to_object_from_table, update_object_quantity_in_table

def test_stock_creation():
    '''
    Tests valid creation of object from table
    '''
    stock = Stock('eggs', 0.5)
    assert stock.name == 'Eggs'
    assert stock.quantity == 0
    assert stock.restock_price == 0.5

def test_restock_add():
    '''
    Tests adding item's amount to stock
    '''
    stock = Stock('ham', 1)
    stock.restock(15, Wallet(99999))
    assert stock.quantity == 15
    stock.restock(15, Wallet(99999))
    assert stock.quantity == 30
    assert stock.quantity != 15

def test_restock_set():
    '''
    Tests setting item's amount to stock
    '''
    stock = Stock('spam', 15)
    stock.restock(15, Wallet(99999), mode='set')
    assert stock.quantity == 15
    stock.restock(15, Wallet(99999), mode='set')
    assert stock.quantity == 15
    assert stock.quantity != 30

def test_restock_add_wallet():
    '''
    Tests subtracting cost of item from wallet
    '''
    stock = Stock('ham', 1)
    wallet = Wallet(50)
    stock.restock(15, wallet)
    assert wallet.money == 35
    stock.restock(15, wallet)
    assert wallet.money == 20

def test_restock_set_wallet():
    '''
    Tests setting wallet money based on previous money in it
    '''
    stock = Stock('spam', 15)
    wallet = Wallet(250)
    stock.restock(15, wallet, mode='set')
    assert wallet.money == 25
    stock.restock(15, wallet, mode='set')
    assert wallet.money == 25
    stock.restock(10, wallet, mode='set')
    assert wallet.money == 100

def test_take_item_from_stock():
    '''
    Tests valid substraction of item's amount from quantity in stock
    '''
    stock = string_to_object_from_table('Ham', Stock)
    assert stock.quantity == 30
    update_object_quantity_in_table(stock.name, Stock, stock.quantity-2)
    stock = string_to_object_from_table('Ham', Stock)
    assert string_to_object_from_table('Ham', Stock).quantity == 28
    update_object_quantity_in_table(stock.name, Stock, stock.quantity+2)
    stock = string_to_object_from_table('Ham', Stock)
    assert string_to_object_from_table('Ham', Stock).quantity == 30    