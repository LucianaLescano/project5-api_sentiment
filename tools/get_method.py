from config.configuration import db, IV, V, VI


# Funciones para hacer queries a la base de datos de donde obtendremos
# la información que el usuario pide

############### First query

def get_dialogues_from_IV(character):
    '''
    Query a la base de datos para sacar todos los dialogos del personaje
    elegido de la colección IV
    '''
    query = {"character":f"{character}"}
    dialogues_list = list(IV.find(query, {"_id":0}))
    return dialogues_list


def get_dialogues_from_V(character):
    '''
    Query a la base de datos para sacar todos los dialogos del personaje
    elegido de la colección V
    '''
    query = {"character":f"{character}"}
    dialogues_list = list(V.find(query, {"_id":0}))
    return dialogues_list


def get_dialogues_from_VI(character):
    '''
    Query a la base de datos para sacar todos los dialogos del personaje
    elegido de la colección VI
    '''
    query = {"character":f"{character}"}
    dialogues_list = list(VI.find(query, {"_id":0}))
    return dialogues_list

############### Second query

def all_characters_from_IV():
    '''
    Query a la base de datos para sacar todos los personajes de la 
    colección IV
    '''
    query = "character"
    characters_list = list(IV.distinct(query))
    return characters_list 


def all_characters_from_V():
    '''
    Query a la base de datos para sacar todos los personajes de la 
    colección V
    '''
    query = "character"
    characters_list = list(V.distinct(query))
    return characters_list 


def all_characters_from_VI():
    '''
    Query a la base de datos para sacar todos los personajes de la 
    colección VI
    '''
    query = "character"
    characters_list = list(VI.distinct(query))
    return characters_list    

############### Third query 

def all_dialogues_from_IV():
    '''
    Query a la base de datos para sacar todos los dialoos de la 
    colección IV
    '''
    query = "dialogue"
    dialogues_list = list(IV.distinct(query))
    return dialogues_list 


def all_dialogues_from_V():
    '''
    Query a la base de datos para sacar todos los dialoos de la 
    colección V
    '''
    query = "dialogue"
    dialogues_list = list(V.distinct(query))
    return dialogues_list 


def all_dialogues_from_VI():
    '''
    Query a la base de datos para sacar todos los dialoos de la 
    colección VI
    '''
    query = "dialogue"
    dialogues_list = list(VI.distinct(query))
    return dialogues_list 