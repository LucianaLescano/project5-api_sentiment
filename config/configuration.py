import os
import dotenv 
from pymongo import MongoClient 


# Cargando la variable de entorno, donde tenemos el URL
# de nuestra base de datos

dotenv.load_dotenv()
DBURL = os.getenv("URL")

if not (DBURL):
    raise ValueError("Please, provide an URL")

# Abrimos una instacia en MongoDB

client = MongoClient(DBURL)
db = client.get_database()
IV = db["IV"]
V = db["V"]
VI = db["VI"]