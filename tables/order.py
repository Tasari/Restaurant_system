from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from tables.order_product import Order_Product
from tools import string_to_object_from_table
from tables.products import Product

from base_template import Base, Session, engine

class Order(Base):
    '''
    Table holding orders 
    '''
    __tablename__ = 'orders'

    id = Column(Integer, primary_key = True)
    order = relationship('Order_Product')
    price = Column(Float)
    date = Column(Date)
    worker_id = Column(Integer, ForeignKey('workers.id'))

    def __init__(self):
        self.order = []
        self.price = 0
        self.date = date.today()
    
    def add_product_to_order(self, product, amount):
        '''
        Adds Product and its amount to the order

        Parameters:
            product (str): Name of the product to be used in order
            amount (int): Amount of given product to be used in order
        '''
        self.order.append((Order_Product(product, amount)))

    def count_price(self):
        '''
        Count sum price of products in order and saves it
        '''
        self.price = 0
        for item_and_amount in self.order:
            item = item_and_amount.ordered_product
            amount = item_and_amount.amount
            for i in range(amount):
                self.price += item.price

    def finish_order(self, wallet, worker):
        '''
        Finishes order, counts money, 
        subtracts recipe from stock, adds it to wallet,
        and adds the order to the worker

        Parameters:
            wallet (Wallet): Wallet object which will get the money from order
            worker (Worker): Worker who completes the order
        '''
        self.count_price()
        self.subtract_ordered_products_recipe_from_stock
        wallet.add_money(self.price)
        worker.orders.append(self)

    def subtract_ordered_products_recipe_from_stock(self):
        '''
        Function substracting recipe of each product in order
        from stock
        '''
        for product_and_amount in self.order:
            product = string_to_object_from_table(product_and_amount.ordered_product.name, Product)
            for i in range(product_and_amount.amount):
                product.remove_ingredients_from_stock()

    def __del__(self):
        '''
        Saves order to database
        '''
        session = Session()
        session.add(self)
        session.commit()
        session.close()