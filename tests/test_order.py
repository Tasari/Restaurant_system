import unittest.mock
from order import Order
from products import Products
from recipes import Recipe
from stock import Stock
from order_product import Order_Product

def test_order_creation_test():
    order = Order()
    assert order.order == []
    assert order.price == 0

def test_order_add_test():
    order = Order()
    order.add_product_to_order('french fries', 1)
    order.add_product_to_order('hamBurgEr', 1)
    assert order.order[0].ordered_product.name == 'French Fries'