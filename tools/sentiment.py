from config.configuration import db, IV, V, VI
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#nltk.download('vader_lexicon')
#nltk.download('punkt')
#nltk.download('stopwords')


# Funciones para hacer queries a la base de datos de donde obtendremos
# la información que el usuario pide

############### First query

def getting_sentiment_from_IV(character):
    '''
    Query a la base de datos para sacar la polaridad de los dialogos 
    del personaje elegido de la colección IV
    '''
    query = {"character":f"{character}"}
    dialogues_list = list(IV.find(query, {"_id":0, "character":0}))
    final = []
    for d in dialogues_list:
        polarity_list = []
        polarity_list.append(d)
        sia = SentimentIntensityAnalyzer()
        polarity = sia.polarity_scores(d['dialogue'])
        polarity_list.append(polarity)
        final.append(polarity_list)
    return final


def getting_sentiment_from_V(character):
    '''
    Query a la base de datos para sacar la polaridad de los dialogos 
    del personaje elegido de la colección V
    '''
    query = {"character":f"{character}"}
    dialogues_list = list(V.find(query, {"_id":0, "character":0}))
    final = []
    for d in dialogues_list:
        polarity_list = []
        polarity_list.append(d)
        sia = SentimentIntensityAnalyzer()
        polarity = sia.polarity_scores(d['dialogue'])
        polarity_list.append(polarity)
        final.append(polarity_list)
    return final

def getting_sentiment_from_VI(character):
    '''
    Query a la base de datos para sacar la polaridad de los dialogos 
    del personaje elegido de la colección VI
    '''
    query = {"character":f"{character}"}
    dialogues_list = list(VI.find(query, {"_id":0, "character":0}))
    final = []
    for d in dialogues_list:
        polarity_list = []
        polarity_list.append(d)
        sia = SentimentIntensityAnalyzer()
        polarity = sia.polarity_scores(d['dialogue'])
        polarity_list.append(polarity)
        final.append(polarity_list)
    return final


############### Second query

def getting_all_sentiment_from_IV():
    '''
    Query a la base de datos para sacar la polaridad de todos los dialogos 
    de la colección IV
    '''
    query = "dialogue"
    dialogues_list = list(IV.distinct(query))
    final = []
    for d in dialogues_list:
        polarity_list = []
        polarity_list.append(d)
        sia = SentimentIntensityAnalyzer()
        polarity = sia.polarity_scores(d)
        polarity_list.append(polarity)
        final.append(polarity_list)
    return final


def getting_all_sentiment_from_V():
    '''
    Query a la base de datos para sacar la polaridad de todos los dialogos 
    de la colección V
    '''
    query = "dialogue"
    dialogues_list = list(V.distinct(query))
    final = []
    for d in dialogues_list:
        polarity_list = []
        polarity_list.append(d)
        sia = SentimentIntensityAnalyzer()
        polarity = sia.polarity_scores(d)
        polarity_list.append(polarity)
        final.append(polarity_list)
    return final


def getting_all_sentiment_from_VI():
    '''
    Query a la base de datos para sacar la polaridad de todos los dialogos 
    de la colección VI
    '''
    query = "dialogue"
    dialogues_list = list(VI.distinct(query))
    final = []
    for d in dialogues_list:
        polarity_list = []
        polarity_list.append(d)
        sia = SentimentIntensityAnalyzer()
        polarity = sia.polarity_scores(d)
        polarity_list.append(polarity)
        final.append(polarity_list)
    return final