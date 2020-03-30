from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base_template import Base

class Recipe(Base):
    __tablename__ = 'recipes'
    
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    stock_id = Column(Integer, ForeignKey('stock.id'), primary_key = True)
    ingredients = relationship('Stock')
    amount = Column(Integer)

    def __init__(self, ingredients, amount):
        self.amount = amount
        self.ingredients = ingredients