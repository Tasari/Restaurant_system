from tables.order_product import Order_Product

def test_order_product_creation():
    order_product = Order_Product('HambUrger', 5)
    assert order_product.amount == 5
    assert order_product.ordered_product.name == 'Hamburger'
    