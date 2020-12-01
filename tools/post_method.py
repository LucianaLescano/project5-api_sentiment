from config.configuration import db, IV, V, VI


# Funciones para hacer queries a la base de datos donde introduciremos
# la información que el usuario quiere


def new_entry_to_IV(character, dialogue):
    '''
    Función para agregar una nueva entrada a la colección IV de la base de datos
    '''
    query_one = {"character" : f"{character}"}
    query_two = {"dialogue" : f"{dialogue}"}
    response = list(IV.find({"$and":[query_one,query_two]},{"character":1, "dialogue":1, "_id":0}))
    try:
        if response == []:
            dict_insert = { 
                "character" : f"{character}",
                "dialogue" : f"{dialogue}"
            }
            IV.insert_one(dict_insert)
    except:
        raise ValueError("Repeated entry")


def new_entry_to_V(character, dialogue):
    '''
    Función para agregar una nueva entrada a la colección V de la base de datos
    '''
    query_one = {"character" : f"{character}"}
    query_two = {"dialogue" : f"{dialogue}"}
    response = list(V.find({"$and":[query_one,query_two]},{"character":1, "dialogue":1, "_id":0}))
    try:
        if response == []:
            dict_insert = { 
                "character" : f"{character}",
                "dialogue" : f"{dialogue}"
            }
            V.insert_one(dict_insert)
    except:
        raise ValueError("Repeated entry")


def new_entry_to_VI(character, dialogue):
    '''
    Función para agregar una nueva entrada a la colección VI de la base de datos
    '''
    query_one = {"character" : f"{character}"}
    query_two = {"dialogue" : f"{dialogue}"}
    response = list(VI.find({"$and":[query_one,query_two]},{"character":1, "dialogue":1, "_id":0}))
    try:
        if response == []:
            dict_insert = { 
                "character" : f"{character}",
                "dialogue" : f"{dialogue}"
            }
            VI.insert_one(dict_insert)
    except:
        raise ValueError("Repeated entry")
