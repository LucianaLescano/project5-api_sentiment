<div style="text-align:center"><img src="https://img.cinemablend.com/cb/f/8/5/4/0/a/f8540aac64ee6cd1412906b2be8c19052c788d9263a8be5d3853facf11aa91b0.jpg" height=400 /></div>

# Api Sentiment 

This week's project is all about creating our own API and be the data provider 🥳.

Here you will find my Star Wars Scripts API, where you can ask for the characters and its dialogues. Also, if you want you can add new dialogues between different characters.

### About my MongoDB database

The database has three collections each one of them represeants a Star Wars movie. 

- Collection 1 - SW Episode IV 
- Collection 2 - SW Episode V
- Collection 3 - SW Episode VI

### Post Request 

#### New entry

A new entry will be added to an existing collection in MongoDB database. 

- Endpoint: 

    You must choose an endpoint based on what collection you want to add a new entry.

    http://127.0.0.1:5000/IV/newentry

    http://127.0.0.1:5000/V/newentry

    http://127.0.0.1:5000/VI/newentry

- Query parameters: 

    No parameters needed.

- To add:

    A dictionary with the character and dialogue values. As shown below:

    ```
    {'character': 'THREEPIO',
    'dialogue': "Did you hear that?  They've shut down the main reactor.  We'll be destroyed for sure.  This is madness!"}
    ```

- Response:

    If you suceed on loading a new entry you will receive:  “New entry successfully registered in the database”
    Due to we do not want repeated entries an error will be raise if that occurs: "Repeated entry”


### Get Request

#### Dialogues 

You will receive all the messages from a certain character.
 
- Endpoint: 

    You must choose an endpoint based on what collection you want to receive information about:

    http://127.0.0.1:5000/IV/

    http://127.0.0.1:5000/V/

    http://127.0.0.1:5000/VI/

- Query parameters:

    - character : required string

- Response:

    If you suceed, you will receive all the entries with the dialogues that match de character introduced.

#### All the dialogues 

You will receive all the messages from the collection.
 
- Endpoint: 

    You must choose an endpoint based on what collection you want to receive information about:

    http://127.0.0.1:5000/IV/all/characters

    http://127.0.0.1:5000/V/all/characters

    http://127.0.0.1:5000/VI/all/characters

- Query parameters:

    No parameters needed.

- Response:

    If you suceed, you will receive all the entries with the dialogues from a certain collection.

#### All the characters

You will receive all the characters from the collection.
 
- Endpoint: 

    You must choose an endpoint based on what collection you want to receive information about:

    http://127.0.0.1:5000/IV/all/dialogues

    http://127.0.0.1:5000/V/all/dialogues

    http://127.0.0.1:5000/VI/all/dialogues

- Query parameters:

    No parameters needed.

- Response:

    If you suceed, you will receive all the different characters from a certain collection.

#### Sentiment from characters

You will receive the messages and an analisis of its emotional value from a certain character.
 
- Endpoint: 

    You must choose an endpoint based on what collection you want to receive information about:

    http://127.0.0.1:5000/IV/sentiment/

    http://127.0.0.1:5000/V/sentiment/

    http://127.0.0.1:5000/VI/sentiment/

- Query parameters:

    - character : required string

- Response:

    If you suceed, you will receive the entries with the dialogues and the analisis that match de character introduced.

#### Sentiment from all characters

You will receive all the messages and an analisis of its emotional value from the collection.
 
- Endpoint: 

    You must choose an endpoint based on what collection you want to receive information about:

    http://127.0.0.1:5000/IV/sentiment/all/dialogues

    http://127.0.0.1:5000/IV/sentiment/all/dialogues

    http://127.0.0.1:5000/IV/sentiment/all/dialogues

- Query parameters:

    No parameters needed.

- Response:

    If you suceed, you will receive all the entries with the dialogues and the analisis from the collection.

### All about this project

#### How? 🧐

I was able to do this thanks to a database of three Star Wars movies, it has all the dialogues and characters from each movie.
You cand find it [here](https://www.kaggle.com/xvivancos/star-wars-movie-scripts).

#### What did I did? 🤔

Creating an API to serve different data to users who want to get this data or maybe collaborate with me posting new data.

All the resources used:

- Flask ([documentation](https://flask.palletsprojects.com/en/1.1.x/))
- Pandas ([documentation](https://pandas.pydata.org/docs/))
- Pymongo ([documentation](https://pymongo.readthedocs.io/en/stable/))
- Requests ([documentation](https://requests.readthedocs.io/en/master/))
- NLTK ([documentation](https://www.nltk.org))

#### As always

Feel free to tell me anything you think will help me or my code be better analyts. 