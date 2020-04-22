from base_template import Session

def name_changer(name):
    '''
    Function changing all words in given string 
    to have 1st letter capitalized and next small
    Parameters:
        name (str): name which will be normalized
    '''
    new_name = ''
    words_in_name = name.split()
    for word in words_in_name:
        new_name += (str(word[0].upper() + word[1:].lower()) + ' ')
    return new_name[:-1]

def string_to_object_from_table(name, table):
    '''
    Function returning object with given name from table
    Parameters:
        name (str): Name of item which will be normalized and searched
        table (Table): Table in which name will be searched
    '''
    session = Session()
    ingredient_obj = session.query(table).filter(table.name == name_changer(name)).first()
    if ingredient_obj is None:
        return 0
    session.close()
    return ingredient_obj

def update_object_quantity_in_table(name, table, new_quantity):
    session = Session()
    session.ingredient_obj = session.query(table).\
        filter(table.name == name_changer(name)).\
            update({table.quantity: new_quantity}, synchronize_session=False)
    session.commit()