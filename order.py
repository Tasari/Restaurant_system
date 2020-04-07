from sqlalchemy import Column, Integer, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from datetime import date
from tools import name_changer, string_to_object_from_db
from products import Products
from order_product import Order_Product

from base_template import Base, Session

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key = True)
    order = relationship('Order_Product')
    price = Column(Float)
    date = Column(Date)

    def __init__(self):
        self.session = Session()
        self.order = []
        self.price = 0
        self.date = date.today()
        for item_and_amount in self.order:
            item = item_and_amount[0]
            amount = item_and_amount[1]
            for i in range(amount):
                self.price += item.price
    
    def add_product_to_order(self, product, amount):
        prod_obj = string_to_object_from_db(product, Products, self.session)
        try:
            assert prod_obj != 0
        except AssertionError:
            print('No Object')
            return
        self.order.append((Order_Product(prod_obj, amount)))

    def __del__(self):
        pass