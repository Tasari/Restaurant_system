from products import Products
from stock import Stock
from recipes import Recipe
from tools import name_changer, string_to_object_from_db

from base_template import Session, engine, Base

Base.metadata.create_all(engine)

def add_to_stock(name, cost):
    '''
    Function adding to stock database
    '''
    session = Session()
    name = name_changer(name)
    if is_in_stock(name, session):
        return 1
    session.add(Stock(name, cost))
    session.commit()
    session.close()
    return 0

def is_in_stock(name, session):
    '''
    Function checking if object with given name is in stock
    '''
    if session.query(Products).filter(Stock.name == name).all() != []:
        return 1
    return 0

def add_product(name, cost, recipe):
    '''
    Recipe has to be a list of lists, 
    where 1st element is the name of item in stock 
    and second is the amount of given ingredient
    Valid use: add_product(name, 
                cost, 
                [['ingredient1', amount_of_ingredient1], ['ingredient2', amount_of_ingredient2]])
    '''
    session = Session()
    name = name_changer(name)
    if is_a_product(name, session):
        return 1
    session.add(Products(name, 
                         cost, 
                         [Recipe(string_to_object_from_db(name_changer(ingre_name), Stock, session), int(amount)) for ingre_name, amount in recipe]))
    session.commit()
    session.close()
    return 0

def is_a_product(name, session):
    '''
    Checks if name is in products database
    '''
    if session.query(Products).filter(Products.name == name).all() != []:
        return 1
    return 0
