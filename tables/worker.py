from sqlalchemy import Column, Integer, Numeric, String
from sqlalchemy.orm import relationship
from tools import name_changer

from base_template import Base, Session

class Worker(Base):
    '''
    Table holding workers
    '''
    __tablename__ = 'workers'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    rank = Column(Integer)
    work_hours = Column(Integer)
    hourly_rate = Column(Numeric(scale=2))
    orders = relationship('Order')


    def __init__(self, name):
        '''
        Creates worker normalizing the name
        Parameters:
            name (str): Name and surname of the worker
        '''
        self.name = name_changer(name)
        self.rank = 0
        self.orders = []
        self.work_hours = 0
        self.hourly_rate = 15
    
    def promotion(self, ranks=1):
        '''
        Promotes the worker, by default promotes 1 rank up,
        demotion by using -1
        Parameters:
            ranks (int): How many ranks shoud worker advance
        '''
        self.rank += ranks
        self.hourly_rate = float(self.hourly_rate) + ranks*1.5
    
    def add_work_hours(self, hours):
        '''
        Adds work hours to worker
        Parameters:
            hours (int): How many hours worker worked
        '''
        self.work_hours += hours

    def orders_price_sum(self):
        '''
        Returns how many money worker earned
        summing price of all orders finished by him.
        '''
        all_orders_sum = 0
        for order in self.orders:
            all_orders_sum += order.price
        return float(all_orders_sum)
        