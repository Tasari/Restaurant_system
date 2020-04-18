from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import relationship
from tools import name_changer

from base_template import Base, Session

class Worker(Base):
    __tablename__ = 'workers'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    rank = Column(Integer)
    work_hours = Column(Integer)
    orders = relationship('Order')
    

    def __init__(self, name):
        self.name = name_changer(name)
        self.rank = 0
        self.orders = []
        self.work_hours = 0
    
    def promotion(self, ranks=1):
        self.rank += ranks

    def add_work_hours(self, hours):
        self.work_hours += hours

    def orders_price_sum(self):
        all_orders_sum = 0
        for order in self.orders:
            all_orders_sum += order.price