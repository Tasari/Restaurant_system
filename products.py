from sqlalchemy import String, Integer, Column, Table, ForeignKey, Float
from sqlalchemy.orm import relationship

from base_template import Base, Session

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    name = Column(String, unique=True)
    price = Column(Float)
    recipe = relationship('Stock')

    def __init__(self, name, price):
        self.name = name
        self.price = price