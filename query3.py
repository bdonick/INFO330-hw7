#Write a query that returns all the Pokemon with an ability of "Overgrow" (1pt)
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

print("\n\nRunning query 3 (overgrow query)\n")

overgrow = {"abilities": {"$regex": "Overgrow"}}
findOvergrow = pokemonColl.find(overgrow)
for pokemon in findOvergrow:
    print(pokemon)

print("\nRunning query 3 (overgrow query)\n\n")

mongoClient.close()