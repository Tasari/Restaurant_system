from sqlalchemy import String, Integer, Column, Table, ForeignKey
from sqlalchemy.orm import relationship

from base_template import Base

recipes = Table(
    'recipes', 
    Base.metadata,
    Column('item', String, ForeignKey('menu.name')),
    Column('ingredients', String, ForeignKey('stock.name'))
)

class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Integer)
    recipe = relationship('Recipe', secondary = recipes)

    def __init__(self, name, price):
        self.name = name
        self.price = price