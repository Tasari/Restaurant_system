from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from datetime import date
from tables.order_product import Order_Product

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
        Finishes order, counts money and adds it to wallet,
        and adds the order to the worker

        Parameters:
            wallet (Wallet): Wallet object which will get the money from order
            worker (Worker): Worker who completes the order
        '''
        self.count_price()
        wallet.add_money(self.price)
        worker.orders.append(self)

    def __del__(self):
        '''
        Saves order to database
        '''
        session = Session()
        session.add(self)
        #allows usage of order after commit
        session.expunge_all()
        session.commit()
        session.close()