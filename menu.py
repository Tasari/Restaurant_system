from sqlalchemy import String, Integer, Column, Table, ForeignKey, Float
from sqlalchemy.orm import relationship

from base_template import Base, Session

class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    price = Column(Float)
    recipe = relationship('Stock')

    def __init__(self, name, price):
        self.name = name
        self.price = price