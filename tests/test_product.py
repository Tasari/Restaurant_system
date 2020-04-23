from tables.products import Product
from tools import string_to_object_from_table
from tables.stock import Stock

def test_product_creation():
    '''
    Tests valid creation of object from table
    '''
    product = Product('cheeseburger', 2.5)
    assert product.name == 'Cheeseburger'
    assert product.price == 2.5
    assert product.recipe == []

def test_product_add():
    '''
    Tests valid adding of single ingredient to recipe of product
    '''
    product = Product('Potato chips', 2.5)
    product.add_ingredient_to_recipe('potato', 2)
    assert product.recipe[0].ingredient.name == 'Potato'
    assert product.recipe[0].amount == 2

def test_many_ingredients_adds():
    '''
    Tests valid adding of multiple ingredients to recipe of product 
    '''
    product = Product('cheeseburger', 2.5)
    product.add_ingredient_to_recipe('cheese', 1)
    product.add_ingredient_to_recipe('meat', 1)
    product.add_ingredient_to_recipe('bun', 2)
    assert product.recipe[0].ingredient.name == 'Cheese'
    assert product.recipe[1].ingredient.name == 'Meat'
    assert product.recipe[2].ingredient.name == 'Bun'
    assert product.recipe[2].amount == 2

def test_remove_ingredients_from_stock():
    product = string_to_object_from_table('hamburger', Product)
    meat = string_to_object_from_table('meat', Stock)
    bun = string_to_object_from_table('bun', Stock)
    product.remove_ingredients_from_stock()
    assert meat.quantity-1 == string_to_object_from_table('meat', Stock).quantity
    assert bun.quantity-2 == string_to_object_from_table('bun', Stock).quantity