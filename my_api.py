from flask import Flask, request
import markdown.extensions.fenced_code
import json
import tools.get_method as get
import tools.post_method as pos
import tools.sentiment as sen

# Endpoints para nuesta API

app = Flask(__name__)


# Devuelve el contenido del README
@app.route("/")
def index():
    readme_file = open("README.md")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string



##################### GET #####################

############### First query

# Devuelve todos los mensajes del personaje elegido de la colección IV
@app.route("/IV/<character>")
def get_dialogues_from_IV(character):
    all_dialogues = get.get_dialogues_from_IV(character)
    return json.dumps(all_dialogues)


# Devuelve todos los mensajes del personaje elegido de la colección V
@app.route("/V/<character>")
def get_dialogues_from_V(character):
    all_dialogues = get.get_dialogues_from_V(character)
    return json.dumps(all_dialogues)


# Devuelve todos los mensajes del personaje elegido de la colección VI
@app.route("/VI/<character>")
def get_dialogues_from_VI(character):
    all_dialogues = get.get_dialogues_from_VI(character)
    return json.dumps(all_dialogues)


############### Second query

# Devuelve todos los personajes de la colección IV
@app.route("/IV/all/characters")
def all_characters_from_IV():
    all_characters = get.all_characters_from_IV()
    return json.dumps(all_characters)


# Devuelve todos los personajes de la colección V
@app.route("/V/all/characters")
def all_characters_from_V():
    all_characters = get.all_characters_from_V()
    return json.dumps(all_characters)


# Devuelve todos los personajes de la colección VI
@app.route("/VI/all/haracters")
def all_characters_from_VI():
    all_characters = get.all_characters_from_VI()
    return json.dumps(all_characters)


############### Third query 

# Devuelve todos los dialogos de la colección IV
@app.route("/IV/all/dialogues")
def all_dialogues_from_IV():
    all_dialogues = get.all_dialogues_from_IV()
    return json.dumps(all_dialogues)


# Devuelve todos los dialogos de la colección V
@app.route("/V/all/dialogues")
def all_dialogues_from_V():
    all_dialogues = get.all_dialogues_from_V()
    return json.dumps(all_dialogues)


# Devuelve todos los dialogos de la colección VI
@app.route("/VI/all/dialogues")
def all_dialogues_from_VI():
    all_dialogues = get.all_dialogues_from_VI()
    return json.dumps(all_dialogues)


############### Fourth query 

# Devuelve la polaridad de todos los mensajes del personaje elegido
# de la colección IV
@app.route("/IV/sentiment/<character>")
def getting_sentiment_from_IV(character):
    sentiment = sen.getting_sentiment_from_IV(character)
    return json.dumps(sentiment)


# Devuelve la polaridad de todos los mensajes del personaje elegido
# de la colección V
@app.route("/V/sentiment/<character>")
def getting_sentiment_from_V(character):
    sentiment = sen.getting_sentiment_from_V(character)
    return json.dumps(sentiment)


# Devuelve la polaridad de todos los mensajes del personaje elegido
# de la colección VI
@app.route("/VI/sentiment/<character>")
def getting_sentiment_from_VI(character):
    sentiment = sen.getting_sentiment_from_VI(character)
    return json.dumps(sentiment)


############### Fifth query 

# Devuelve la polaridad de todos los mensajes de la colección IV
@app.route("/IV/sentiment/all/dialogues")
def getting_all_sentiment_from_IV():
    all_sentiment = sen.getting_all_sentiment_from_IV()
    return json.dumps(all_sentiment)


# Devuelve la polaridad de todos los mensajes de la colección V
@app.route("/V/sentiment/all/dialogues")
def getting_all_sentiment_from_V():
    all_sentiment = sen.getting_all_sentiment_from_V()
    return json.dumps(all_sentiment)


# Devuelve la polaridad de todos los mensajes de la colección VI
@app.route("/VI/sentiment/all/dialogues")
def getting_all_sentiment_from_VI():
    all_sentiment = sen.getting_all_sentiment_from_VI()
    return json.dumps(all_sentiment)


##################### POST #####################


# Nueva entrada en colección ya existente
@app.route("/IV/newentry", methods=["POST"])
def new_entry_to_IV():
    character = request.form.get("character")
    dialogue = request.form.get("dialogue")
    pos.new_entry_to_IV(character, dialogue)
    return "New entry successfully registered in the database"


# Nueva entrada en colección ya existente
@app.route("/V/newentry", methods=["POST"])
def new_entry_to_V():
    character = request.form.get("character")
    dialogue = request.form.get("dialogue")
    pos.new_entry_to_V(character, dialogue)
    return "New entry successfully registered in the database"


# Nueva entrada en colección ya existente
@app.route("/VI/newentry", methods=["POST"])
def new_entry_to_VI():
    character = request.form.get("character")
    dialogue = request.form.get("dialogue")
    pos.new_entry_to_VI(character, dialogue)
    return "New entry successfully registered in the database"
































app.run(debug=True)