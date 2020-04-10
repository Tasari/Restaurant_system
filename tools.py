from base_template import Session, engine
from sqlalchemy import MetaData

def name_changer(name):
    '''
    Function changing all words in given string 
    to have 1st letter capitalized and next small 
    '''
    new_name = ''
    words_in_name = name.split()
    for word in words_in_name:
        new_name += (str(word[0].upper() + word[1:].lower()) + ' ')
    return new_name[:-1]

def string_to_object_from_table(name, table, session):
    '''
    Function returning object with given name from table
    '''
    ingredient_obj = session.query(table).filter(table.name == name).first()
    if ingredient_obj is None:
        return 0
    return ingredient_obj

def is_in_table(name, table):
    '''
    Checks if name is in products table
    '''
    if Session().query(table).filter(table.name == name).all() != []:
        return 1
    return 0