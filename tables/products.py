from sqlalchemy import String, Integer, Column, Table, ForeignKey, Float
from sqlalchemy.orm import relationship

from base_template import Base
from wallet import wallet

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    name = Column(String, unique=True)
    price = Column(Float)
    recipe = relationship('Recipe')

    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe
    
    def __repr__(self):
        return self.name
