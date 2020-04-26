from sqlalchemy import Column, String, Integer, Float
from tools import name_changer

from base_template import Base, Session

class Stock(Base):
    '''
    Table holding data about items in warehouse
    '''

    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    quantity = Column(Integer)
    restock_price = Column(Float)

    def __init__(self, name, restock_price):
        '''
        Creates new item in stock normalizing the name
        Parameters:
            name (str): String representing the name of the item
            restock_price (float): Cost of adding 1 item to the stock
        '''
        self.name = name_changer(name)
        self.quantity = 0
        self.restock_price = restock_price

    def __repr__(self):
        return self.name

    def restock(self, amount, wallet, mode='add'):
        '''
        Adds given amount of item to stock 
        subtracting money from wallet, works in 2 modes
        Parameters:
            amount (int): Amount which you want to add to/in the stock
            wallet (Wallet): Which wallet should be charged
            mode ('add', 'set'): Mode in which should restock work
        Usage:
            restock(amount) - adds given amount to stock and charges given wallet
            restock(amount, wallet, mode='set' - sets given amount in stock and modifies given wallet)
        '''
        if mode == 'add':
            if self.quantity + amount >= 0:
                if wallet.add_money(-amount*self.restock_price):
                    return -4
                self.update_object_quantity_in_Stock(self.quantity + amount)
            else:
                return -1
        elif mode == 'set':
            if amount >= 0:
                if wallet.add_money(-(amount-self.quantity)*self.restock_price):
                    return -4
                self.update_object_quantity_in_Stock(amount)
            else:
                return -2
        else:
            return -3
        
    def update_object_quantity_in_Stock(self, new_quantity):
        '''
        Sets new quantity in stock table
        Parameters:
            name (str): Name of product to be updated
            new_quantity (int): Amount to be set in table
        '''
        session = Session()
        session.ingredient_obj = session.query(Stock).\
            filter(Stock.name == self.name).\
                update({Stock.quantity: new_quantity}, synchronize_session=False)
        session.commit()
    
    def __del__(self):
        '''
        Saves data to table
        '''
        session = Session()
        session.add(self)
        session.commit()
        session.close()
        
