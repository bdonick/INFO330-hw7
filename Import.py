#Import.py

#Query 1: Write a query that returns all the Pokemon named "Pikachu"

import csv
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

with open('pokemon.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        pokemonColl.insert_one(row)

pikachu = pokemonColl.find({"name": "Pikachu"})

for pokemon in pikachu:
    print(pokemon)

#Query 2: Write a query that returns all the Pokemon with an HP stat greater than 150

healthHigh = pokemonColl.find({"attack": {"$gt": 150}})

for pokemon in healthHigh:
    print(pokemon)

#Query 3: Write a query that returns all the Pokemon with an ability of "Overgrow"

overgrow = pokemonColl.find({"abilities": "Overgrow"})

for pokemon in overgrow:
    print(pokemon)