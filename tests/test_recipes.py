from tables.recipes import Recipe

def test_recipe_creation():
    '''
    Tests valid creation of object from table
    '''
    recipe = Recipe('pOtAtO', 45)
    assert recipe.ingredient.name == 'Potato'
    assert recipe.amount == 45
    