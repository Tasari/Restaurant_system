from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from tables.products import Product
from tools import string_to_object_from_table
from base_template import Base

class Order_Product(Base):
    __tablename__ = 'order_product'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key = True)
    ordered_product = relationship('Product')
    amount = Column(Integer)

    def __init__(self, ordered_product, amount):
        self.amount = amount
        prod_obj = string_to_object_from_table(ordered_product, Product)
        try:
            assert prod_obj != 0
        except AssertionError:
            print('No Object')
            return
        self.ordered_product = prod_obj

    def __repr__(self):
        return str(self.ordered_product.__repr__() + ': ' +str(self.amount))