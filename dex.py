
import csv
import json

def search_pokemon(poke_name):
    with open('data/csv/pokemon.csv', 'r') as file:
        csv_reader = csv.DictReader(file)
        #headers = next(csv_reader)# Read the CSV headers

        for row in csv_reader:
          if poke_name.lower() in row['slug'].lower() or str(poke_name) == str(row["id"]):
              json_data = json.loads(json.dumps(row))
              print(type(json_data))
              id=json_data["id"]
              json_data["url"]=f"https://cdn.poketwo.net/images/{id}.png"
              json_data["shiny"]=f"https://cdn.poketwo.net/shiny/{id}.png"
            
              return json_data

    return None  # Return None if the Pokémon name is not found

def pokemon_moves(poke_id):
  with open('data/csv/pokemon_moves.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    #headers = next(csv_reader)
    moves=[]# Read the CSV headers

    for row in csv_reader:
      if str(poke_id) == str(row['pokemon_id']):
          json_data = json.loads(json.dumps(row))
          print(type(json_data))
          moves.append(json_data)
          #json_data["url"]=f"https://cdn.poketwo.net/images/{poke_id}.png"


    

    gg={"id":poke_id,"url":f"https://cdn.poketwo.net/images/{poke_id}.png","moves":moves}  
    return gg

def moves(id):
  with open('data/csv/moves.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    #headers = next(csv_reader)
    #moves=[]# Read the CSV headers

    for row in csv_reader:
      if str(id) == str(row['id']):
          json_data = json.loads(json.dumps(row))
          print(type(json_data))
          return json_data
          #json_data["url"]=f"https://cdn.poketwo.net/images/{poke_id}.png"




    
    return None
def move_effect(id):
  with open('data/csv/move_effect_prose.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    #headers = next(csv_reader)
    #moves=[]# Read the CSV headers

    for row in csv_reader:
      if str(id) == str(row['move_effect_id']):
          json_data = json.loads(json.dumps(row))
          print(type(json_data))
          return json_data


def evolution(id):
  with open('data/csv/evolution.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    #headers = next(csv_reader)
    #moves=[]# Read the CSV headers

    for row in csv_reader:
      if str(id) == str(row['id']) or str(id) == str(row["evolved_species_id"]):
          json_data = json.loads(json.dumps(row))
          print(type(json_data))
          return json_data

def item(id):
  with open('data/csv/items.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    ##headers = next(csv_reader)
    #moves=[]# Read the CSV headers

    for row in csv_reader:
      if str(id) == str(row['id']):
          json_data = json.loads(json.dumps(row))
          print(type(json_data))
          return json_data
          
#id = input("Enter a Pokémon id: ")
#result = evolution(id)

#if result:
#    print(result)
#else:
#    print('Pokémon not found.')
