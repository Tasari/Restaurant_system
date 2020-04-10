from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base_template import Base

class Order_Product(Base):
    __tablename__ = 'order_product'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'), primary_key = True)
    ordered_product = relationship('Products')
    amount = Column(Integer)

    def __init__(self, ordered_product, amount):
        self.amount = amount
        self.ordered_product = ordered_product

    def __repr__(self):
        return str(self.ordered_product.__repr__() + ': ' +str(self.amount))