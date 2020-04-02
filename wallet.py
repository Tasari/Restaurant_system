from sqlalchemy import Column, Date, Float, Integer
from base_template import Base, Session, engine
from datetime import date

class MoneyArchive(Base):
    __tablename__ = 'moneyarchive'

    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True)
    money = Column(Float)

    def __init__(self, money):
        self.date = date.today()
        self.money = money



class wallet():
    Base.metadata.create_all(engine)
    def __init__(self, money):
        self.money = money
    
    def add_money(self, amount):
        self.money += amount

    def add_data_to_archive(self):
        session = Session()
        session.add(MoneyArchive(self.money))
        session.commit()  
        session.close()

wallet(250).add_data_to_archive()