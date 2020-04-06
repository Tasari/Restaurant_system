from sqlalchemy import Column, Integer, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from datetime import date

from base_template import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key = True)
    order = relationship('Order_Product')
    price = Column(Float)
    date = Column(Date)

    def __init__(self, order):
        self.order = order
        self.price = 0
        self.date = date.today()
        for item_and_amount in self.order():
            item = item_and_amount[0]
            amount = item_and_amount[1]
            for i in range(amount):
                self.price += item.price