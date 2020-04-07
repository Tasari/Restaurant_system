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

def string_to_object_from_db(name, db, session):
    '''
    Function returning object with given name from database
    '''
    ingredient_obj = session.query(db).filter(db.name == name).all()
    if ingredient_obj == []:
        return 0
    return ingredient_obj