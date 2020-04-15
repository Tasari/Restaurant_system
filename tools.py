from base_template import Session

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

def string_to_object_from_table(name, table):
    '''
    Function returning object with given name from table
    '''
    session = Session()
    ingredient_obj = session.query(table).filter(table.name == name_changer(name)).first()
    if ingredient_obj is None:
        return 0
    session.close()
    return ingredient_obj
