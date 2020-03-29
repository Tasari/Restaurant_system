from sqlalchemy import String, Integer, Column, Table, ForeignKey, Float
from sqlalchemy.orm import relationship

from base_template import Base, Session

product_stock = Table(
    'product_stock', Base.metadata,
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('stock_id', Integer, ForeignKey('stock.id'))
)

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key = True)
    name = Column(String, unique=True)
    price = Column(Float)
    recipe = relationship('Stock', secondary=product_stock)

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __repr__(self):
        return self.name