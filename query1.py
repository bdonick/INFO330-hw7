#Write a query that returns all the Pokemon named "Pikachu".
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

print("\n\nRunning query 1 (pikachu query)\n")

pikachu_query = {"name": "Pikachu"}
findPikachu = pokemonColl.find(pikachu_query)
for pokemon in findPikachu:
    print(pokemon)

print("\nFinished running query 1 (pikachu query)\n\n")

mongoClient.close()