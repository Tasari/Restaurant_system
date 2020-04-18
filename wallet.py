from sqlalchemy import Column, Date, Float, Integer
from base_template import Base, Session
from datetime import date

class MoneyArchive(Base):
    '''
    Table archiving money given day
    '''
    __tablename__ = 'moneyarchive'

    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True)
    money = Column(Float)

    def __init__(self, money):
        '''
        Saves money amount with actual date
        Parameters:
            money (int): Money which will be saved
        '''
        self.date = date.today()
        self.money = money

class Wallet():
    '''
    Object that holds the money of shop
    '''
    def __init__(self, money):
        '''
        Sets initial money of shop
        Parameters:
            money (int): Money held by the shop at the start
        '''
        self.money = money
    
    def add_money(self, amount):
        '''
        Adds money to the object
        Parameters:
            amount (int): Amount of money to be added to wallet
        '''
        if self.money + amount < 0:
            return 1
        self.money += amount


    def add_data_to_archive(self):
        '''
        Archivising the money in wallet
        '''
        session = Session()
        session.add(MoneyArchive(self.money))
        session.commit()  
        session.close()