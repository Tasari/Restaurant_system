from tables.products import Product

def test_product_creation():
    product = Product('cheeseburger', 2.5)
    assert product.name == 'Cheeseburger'
    assert product.price == 2.5
    assert product.recipe == []

def test_product_add():
    product = Product('Potato chips', 2.5)
    product.add_ingredient_to_recipe('potato', 2)
    assert product.recipe[0].ingredient.name == 'Potato'
    assert product.recipe[0].amount == 2

def test_many_ingredients_adds():
    product = Product('cheeseburger', 2.5)
    product.add_ingredient_to_recipe('cheese', 1)
    product.add_ingredient_to_recipe('meat', 1)
    product.add_ingredient_to_recipe('bun', 2)
    assert product.recipe[0].ingredient.name == 'Cheese'
    assert product.recipe[1].ingredient.name == 'Meat'
    assert product.recipe[2].ingredient.name == 'Bun'
    assert product.recipe[2].amount == 2