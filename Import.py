#Import.py

import sqlite3
from pymongo import MongoClient

import secrets
import string

id_length = 10

conn = sqlite3.connect("pokemon.sqlite")

cursor = conn.cursor()

cursor.execute("SELECT name, pokedex_number, type1, type2, hp, attack, defense, speed, sp_attack, sp_defense, abilities FROM imported_pokemon_data")

pokemon_rows = cursor.fetchall()

cursor.close()
conn.close()

pokemon_list = []

for row in pokemon_rows:
    alphanumeric = string.ascii_letters + string.digits
    random_id = ''.join(secrets.choice(alphanumeric) for _ in range(id_length))

    pokemon_json = {
        "_id": random_id,
        "name": row[0],
        "pokedex_number": int(row[1]),
        "types": [row[2], row[3]],
        "hp": int(row[4]),
        "attack": int(row[5]),
        "defense": int(row[6]),
        "speed": int(row[7]),
        "sp_attack": int(row[8]),
        "sp_defense": int(row[9]),
        "abilities": row[10]
    }
    pokemon_list.append(pokemon_json)

print(pokemon_list)

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

pokemonColl.insert_many(pokemon_list)

print("Data inserted into the 'pokemon_data' collection.")