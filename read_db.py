from base_template import Session
from products import Products
from stock import Stock
from recipes import Recipe

session = Session()

products = session.query(Products).all()
stock = session.query(Stock).all()
recipes = session.query(Recipe).all()

for recipe in recipes:
    print(recipe.product_id, recipe.stock_id, recipe.amount)

for product in products:
    print(product.name, product.price, product.recipe)

for item in stock:
    print(item.name, item.quantity, item.restock_price)