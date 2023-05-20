# Extra Credit: Improve the Battle.py script.

# Improvements for extra credit:
# 1: Else statement to check for a tie
# 2: Edited the battle script to make it "better/more fun" (made it easier to read by adding spacing stuff)
# 3: Stat counter determines if thier is a tie depending on if the pokemon both have the same number of wins
# 4: Created a stat counter which counts how many stats both pokemon are advantagous in. 

import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("\nLet the Pokemon battle begin! ================")
    print("\nWe have a great match between " + pokemon1['name'] + " and " + pokemon2['name'] + "!!!\n")

    p1StatCount = 0
    p2StatCount = 0
    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            p1StatCount += 1
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            p2StatCount += 1
        else:
            print(pokemon1['name'] + " and " + pokemon2['name'] + " are equal for " + stat)

    if p1StatCount > p2StatCount:
        print("\n" + pokemon1['name'] + " had " + str(p1StatCount) + " point(s), while " +
              pokemon2['name'] + " only had " + str(p2StatCount) + " point(s).")
        print("Battle results: " + pokemon1['name'] + " wins!\n\n")
    elif p1StatCount < p2StatCount:
        print("\n" + pokemon2['name'] + " had " + str(p2StatCount) + " point(s), while " +
              pokemon1['name'] + " only had " + str(p1StatCount) + " point(s).")
        print("Battle results: " + pokemon2['name'] + " wins!\n\n")
    else:
        print("\n" + "Both " + pokemon1['name'] + " and " + pokemon2['name'] + " had " + str(p1StatCount) + " points.")
        print("Battle results: " + pokemon1['name'] + " and " + pokemon2['name'] + " are equal!\n\n")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()