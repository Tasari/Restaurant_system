from tools import name_changer, string_to_object_from_table

from tables.products import Product

def test_name_changer():
    assert name_changer('eGgs') == 'Eggs'
    assert name_changer('eggS ham') == 'Eggs Ham'

def test_string_to_object_from_table():
    assert isinstance(string_to_object_from_table('Hamburger', Product), Product) == True
    assert string_to_object_from_table('foobar', Product) == 0
    assert isinstance(string_to_object_from_table('hamBurgeR', Product), Product) == True