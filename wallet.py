from sqlalchemy import Column, Date, Float, Integer
from base_template import Base, Session
from datetime import date

class MoneyArchive(Base):
    __tablename__ = 'moneyarchive'

    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True)
    money = Column(Float)

    def __init__(self, money):
        self.date = date.today()
        self.money = money

class Wallet():
    def __init__(self, money):
        self.money = money
    
    def add_money(self, amount):
        if self.money + amount < 0:
            return 1
        self.money += amount


    def add_data_to_archive(self):
        session = Session()
        session.add(MoneyArchive(self.money))
        session.commit()  
        session.close()