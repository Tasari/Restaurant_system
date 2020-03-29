from base_template import Session
from products import Products
from stock import Stock

session = Session()

products = session.query(Products).all()

for product in products:
    print(product.name, product.price, product.recipe)

stock = session.query(Stock).all()

for item in stock:
    print(item.name, item.quantity, item.restock_price)