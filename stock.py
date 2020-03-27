from sqlalchemy import Column, string, Integer
from base_template import Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    quantity = Column(Integer)
    restock_price = Column(Integer)

    def __init__(self, name, restock_price):
        self.name = name
        self.quantity = 0
        self.restock_price = restock_price