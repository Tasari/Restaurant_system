from tables.order import Order
from tables.order_product import Order_Product
from tables.stock import Stock
from tables.worker import Worker
from wallet import Wallet
from tools import string_to_object_from_table
from base_template import Session

def test_order_creation():
    '''
    Tests valid creation of object from table
    '''
    order = Order()
    assert order.order == []
    assert order.price == 0

def test_order_add():
    '''
    Tests valid addition of product to order
    '''
    order = Order()
    order.add_product_to_order('french fries', 1)
    assert order.order[0].ordered_product.name == 'French Fries'

def test_count_price():
    '''
    Tests valid count of price in order
    '''
    order = Order()
    order.add_product_to_order('french Fries', 4)
    order.count_price()
    assert float(order.price) == 4

def test_multiple_count_price():
    '''
    Asserts that each count gives the same output
    '''
    order = Order()
    order.add_product_to_order('french Fries', 4)
    order.count_price()
    assert order.price == 4
    order.count_price()
    assert order.price == 4

def test_many_products_adds():
    '''
    Tests adding many products to order
    '''
    order = Order()
    order.add_product_to_order('french fries', 145)
    order.add_product_to_order('hamburger', 14)
    assert order.order[0].ordered_product.name == 'French Fries'
    assert order.order[0].amount == 145
    assert order.order[1].ordered_product.name == 'Hamburger'
    assert order.order[1].amount == 14

def test_many_products_count_price():
    '''
    Tests valid counting of price when multiple items are present
    '''
    order = Order()
    order.add_product_to_order('french fries', 145)
    order.add_product_to_order('hamburger', 14)
    order.count_price()
    assert float(order.price) == 170.2

def test_add_order_value_to_wallet():
    '''
    Tests adding money to wallet after order is finished
    '''
    session = Session()
    worker = string_to_object_from_table('Jack Smith', Worker)
    wallet = Wallet(100)
    order = Order()
    order.add_product_to_order('french fries', 1)
    order.add_product_to_order('hamburger', 1)
    worker.finish_order(wallet, order)
    assert float(wallet.money) == 102.8

def test_remove_ingredients_from_stock():
    order = Order()
    order.add_product_to_order('french fries', 2)
    old = string_to_object_from_table('Potato', Stock)
    order.subtract_ordered_products_recipe_from_stock()
    new = string_to_object_from_table('Potato', Stock)
    assert new.quantity == old.quantity-10
