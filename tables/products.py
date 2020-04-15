from sqlalchemy import String, Integer, Column, Float
from sqlalchemy.orm import relationship
from tables.recipes import Recipe
from tools import name_changer

from base_template import Base, Session 

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    name = Column(String, unique=True)
    price = Column(Float)
    recipe = relationship('Recipe')

    def __init__(self, name, price):
        self.name = name_changer(name)
        self.price = price
        self.recipe = []

    def add_ingredient_to_recipe(self, ingredient, amount):
        self.recipe.append((Recipe(ingredient, amount)))

    
    def __str__(self):
        return self.name

    def __del__(self):
        session = Session()
        session.add(self)
        session.commit()
        session.close()