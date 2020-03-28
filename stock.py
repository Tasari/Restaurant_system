from sqlalchemy import Column, String, Integer, ForeignKey
from base_template import Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String, ForeignKey('menu.name'))
    quantity = Column(Integer)
    restock_price = Column(Integer)

    def __init__(self, name, restock_price):
        self.name = name
        self.quantity = 0
        self.restock_price = restock_price

    def __repr__(self):
        return self.name