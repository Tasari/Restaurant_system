from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from tools import string_to_object_from_table, name_changer
from tables.stock import Stock

from base_template import Base, Session

class Recipe(Base):
    __tablename__ = 'recipes'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'), primary_key = True)
    ingredient = relationship('Stock')
    amount = Column(Integer)

    def __init__(self, ingredient, amount):
        self.session = Session()
        self.amount = amount
        self.ingredient = string_to_object_from_table(name_changer(ingredient), Stock, self.session)

    def __repr__(self):
        return self.ingredient.__repr__()