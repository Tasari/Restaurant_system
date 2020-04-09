import unittest.mock
from order import Order
from products import Products
from recipes import Recipe
from stock import Stock
from order_product import Order_Product

def test_order_creation():
    order = Order()
    assert order.order == []
    assert order.price == 0

def test_order_add():
    order = Order()
    order.add_product_to_order('french fries', 1)
    assert order.order[0].ordered_product.name == 'French Fries'

def test_count_price():
    order = Order()
    order.add_product_to_order('french Fries', 4)
    order.count_price()
    assert order.price == 2

def test_multiple_count_price():
    order = Order()
    order.add_product_to_order('french Fries', 4)
    order.count_price()
    assert order.price == 2
    order.count_price()
    assert order.price == 2

def test_many_products_adds():
    order = Order()
    order.add_product_to_order('french fries', 145)
    order.add_product_to_order('hamburger', 14)
    assert order.order[0].ordered_product.name == 'French Fries'
    assert order.order[0].amount == 145
    assert order.order[1].ordered_product.name == 'Hamburger'
    assert order.order[1].amount == 14

def test_many_products_count_price():
    order = Order()
    order.add_product_to_order('french fries', 145)
    order.add_product_to_order('hamburger', 14)
    order.count_price()
    assert order.price == 93.5