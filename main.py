from flask import Flask, request
from dex import search_pokemon,pokemon_moves,moves,move_effect,evolution,item
app = Flask(__name__)



@app.route('/pokemon', methods=['GET', 'POST'])
def pokemon():
    # Handle GET requests
    if request.method == 'GET':
        # Get the query parameter ‘pokename’ from the URL
        name = request.args.get('pokename')
        if name:
            # Call the search_pokemon function and return the result
            return search_pokemon(name)
        else:
            return"Please provide a valid 'pokename' query parameter"

    # Handle POST requests
    if request.method == 'POST':
        # Get the ‘pokename’ from the request body
        name = request.json.get('pokename')
        if name:
            # Call the search_pokemon function and return the result
            return search_pokemon(name)
        else:
             return "Please provide a valid ‘pokename’ in the request body."

@app.route('/pokemoves', methods=['GET', 'POST'])
def pokemoves():
    # Handle GET requests
    if request.method == 'GET':
        # Get the query parameter ‘pokename’ from the URL
        name = request.args.get('pokeid')
        if name:
            # Call the search_pokemon function and return the result
            return pokemon_moves(name)
        else:
            return"Please provide a valid 'pokeid' query parameter"

    # Handle POST requests
    if request.method == 'POST':
        # Get the ‘pokename’ from the request body
        name = request.json.get('pokeid')
        if name:
            # Call the search_pokemon function and return the result
            return pokemon_moves(name)
        else:
             return "Please provide a valid ‘pokeid’ in the request body."

@app.route('/move', methods=['GET', 'POST'])
def movess():
    # Handle GET requests
    if request.method == 'GET':
        # Get the query parameter ‘pokename’ from the URL
        name = request.args.get('moveid')
        if name:
            # Call the search_pokemon function and return the result
            return moves(name)
        else:
            return"Please provide a valid 'moveid' query parameter"

    # Handle POST requests
    if request.method == 'POST':
        # Get the ‘pokename’ from the request body
        name = request.json.get('moveid')
        if name:
            # Call the search_pokemon function and return the result
            return moves(name)
        else:
             return "Please provide a valid ‘moveid’ in the request body."


@app.route('/moveeffect', methods=['GET', 'POST'])
def moveeffct():
    # Handle GET requests
    if request.method == 'GET':
        # Get the query parameter ‘pokename’ from the URL
        name = request.args.get('moveeffectid')
        if name:
            # Call the search_pokemon function and return the result
            return move_effect(name)
        else:
            return"Please provide a valid 'moveeffectid' query parameter"

    # Handle POST requests
    if request.method == 'POST':
        # Get the ‘pokename’ from the request body
        name = request.json.get('moveeffectid')
        if name:
            # Call the search_pokemon function and return the result
            return move_effect(name)
        else:
             return "Please provide a valid ‘moveeffectid’ in the request body."


@app.route('/evolution', methods=['GET', 'POST'])
def evolutionn():
    # Handle GET requests
    if request.method == 'GET':
        # Get the query parameter ‘pokename’ from the URL
        name = request.args.get('pokeid')
        if name:
            # Call the search_pokemon function and return the result
            return evolution(name)
        else:
            return"Please provide a valid 'pokeid' query parameter"

    # Handle POST requests
    if request.method == 'POST':
        # Get the ‘pokename’ from the request body
        name = request.json.get('pokeid')
        if name:
            # Call the search_pokemon function and return the result
            return evolution(name)
        else:
             return "Please provide a valid ‘pokeid’ in the request body."

@app.route('/item', methods=['GET', 'POST'])
def itemss():
    # Handle GET requests
    if request.method == 'GET':
        # Get the query parameter ‘pokename’ from the URL
        name = request.args.get('itemid')
        if name:
            # Call the search_pokemon function and return the result
            return item(name)
        else:
            return"Please provide a valid 'itemid' query parameter"

    # Handle POST requests
    if request.method == 'POST':
        # Get the ‘pokename’ from the request body
        name = request.json.get('itemid')
        if name:
            # Call the search_pokemon function and return the result
            return item(name)
        else:
             return "Please provide a valid ‘itemid’ in the request body."


@app.route('/', methods=['GET', 'POST'])
def main():
    # Handle GET requests
    return """/pokemon\n/pokemoves\n/move\n/moveeffect\n/evolution\n/item"""

app.run("0.0.0.0",port=1337,debug=True)

