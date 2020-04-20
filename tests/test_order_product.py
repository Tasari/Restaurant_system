from tables.order_product import Order_Product

def test_order_product_creation():
    '''
    Tests valid creation of object from table
    '''
    order_product = Order_Product('HambUrger', 5)
    assert order_product.amount == 5
    assert order_product.ordered_product.name == 'Hamburger'
    