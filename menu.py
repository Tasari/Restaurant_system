from sqlalchemy import String, Integer, Column, Table, ForeignKey
from sqlalchemy.orm import relationship

from base_template import Base

class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Integer)
    recipe = relationship('Stock')

    def __init__(self, name, price):
        self.name = name
        self.price = price
