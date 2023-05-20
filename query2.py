#Write a query that returns all the Pokemon with an attack greater than 150.
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

print("\n\nRunning query 2 (attack greater than 150 query)\n")

attack = {"attack": {"$gt": 150}}
findAttack = pokemonColl.find(attack)
for pokemon in findAttack:
    print(pokemon)

print("\nFinished running query 2 (attack greater than 150 query)\n\n")

mongoClient.close()