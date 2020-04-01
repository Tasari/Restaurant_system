from sqlalchemy import Column, String, Integer, ForeignKey, Float
from base_template import Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    quantity = Column(Integer)
    restock_price = Column(Float)

    def __init__(self, name, restock_price):
        self.name = name
        self.quantity = 0
        self.restock_price = restock_price

    def __repr__(self):
        return self.name

    def restock(self, amount, mode='add'):
        '''
        restock(amount) - adds given amount to stock
        restock(amount, mode='set' - sets given amount in stock)
        '''
        if mode == 'add':
            if self.quantity + amount >= 0:
                self.quantity += amount
            else:
                return -1
        elif mode == 'set':
            if amount >= 0:
                self.quantity = amount
            else:
                return -2
        else:
            return -3