from tools import name_changer, string_to_object_from_table

from tables.products import Product
from tables.stock import Stock

def test_name_changer():
    '''
    Tests valid change of name
    '''
    assert name_changer('eGgs') == 'Eggs'
    assert name_changer('eggS ham') == 'Eggs Ham'

def test_string_to_object_from_table():
    '''
    Tests valid taking item from it's table
    '''
    assert isinstance(string_to_object_from_table('Hamburger', Product), Product) == True
    assert string_to_object_from_table('foobar', Product) == 0
    assert isinstance(string_to_object_from_table('hamBurgeR', Product), Product) == True

def test_update_quantity_in_Stock():
    '''
    Test valid update table data
    '''
    potato = string_to_object_from_table('Potato', Stock)
    potato.update_object_quantity_in_Stock(200)
    assert string_to_object_from_table('Potato', Stock).quantity == 200