from flask import Flask, request
from main import search_pokemon
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
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

if __name__ =="main":
  app.run("0,debug=True)
