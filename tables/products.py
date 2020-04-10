from sqlalchemy import String, Integer, Column, Table, ForeignKey, Float
from sqlalchemy.orm import relationship
from tables.stock import Stock
from tables.recipes import Recipe
from tools import string_to_object_from_table, name_changer

from base_template import Base, Session
from wallet import wallet

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    name = Column(String, unique=True)
    price = Column(Float)
    recipe = relationship('Recipe')

    def __init__(self, name, price):
        self.session = Session()
        self.name = name_changer(name)
        self.price = price
        self.recipe = []

    def add_ingredient_to_recipe(self, ingredient, amount):
        ingre_obj = string_to_object_from_table(name_changer(ingredient), Stock, self.session)
        try:
            assert ingre_obj != 0
        except AssertionError:
            print('No Object')
            return
        self.recipe.append((Recipe(ingre_obj, amount)))

    
    def __repr__(self):
        return self.name

    def __del__(self):
        self.count_price()
        session = self.session
        self.session = None
        session.add(self)
        session.commit()
        session.close()