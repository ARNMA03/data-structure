import numpy as np
import random as rm
from tabulate import tabulate

# Define Pokémon data as an array of dictionaries with dtype=object
pokemon_data = np.array([
    {"name": "Jigglypuff", "power": 25, "health": 100, "poison": 10, "heal": 20, "type": "Normal"},
    {"name": "Pikachu", "power": 25, "health": 100, "poison": 10, "heal": 20, "type": "Electric"},
    {"name": "Eevee", "power": 25, "health": 100, "poison": 10, "heal": 20, "type": "Normal"},
    {"name": "Charmander", "power": 30, "health": 100, "poison": 10, "heal": 20, "type": "Fire"},
    {"name": "Squirtle", "power": 30, "health": 100, "poison": 10, "heal": 20, "type": "Water"},
    {"name": "Bulbasaur", "power": 30, "health": 100, "poison": 10, "heal": 20, "type": "Grass"},
    {"name": "Gengar", "power": 35, "health": 100, "poison": 10, "heal": 20, "type": "Poison"},
    {"name": "Machamp", "power": 40, "health": 100, "poison": 10, "heal": 20, "type": "Fighting"},
    {"name": "Snorlax", "power": 40, "health": 100, "poison": 10, "heal": 20, "type": "Normal"},
    {"name": "Mewtwo", "power": 45, "health": 100, "poison": 10, "heal": 20, "type": "Psychic"}
], dtype=object) 
element = {
    "Electric": [["Water"], ["None"]],
    "Fire": [["Grass"], ["Water", "Fire"]],
    "Water": [["Fire"], ["Electric", "Grass"]],
    "Normal": [["None"], ["None"]],
    "Fighting": [["Normal"], ["Psychic"]],
    "Psychic": [["Fighting"], ["None"]],
    "Grass": [["Water"], ["Fire"]],
    "Poison": [["Grass"], ["Poison", "Psychic"]],
}

p1 = []
p2 = []
battle = []
battled_pokemon = set()
battle_counter = 0
grant = 5
fatigue = 2

while True:
    action = input(" Welcome players!\n'png' to Play New Game(New character) or \n'pa' to Play Again(Same set of characters) or \n any character to exit \n type the letter of the operation you want to do: ").lower()
    if action == "png":
        pokemon_data = np.array([
            {"name": "Jigglypuff", "power": 25, "health": 100, "poison": 10, "heal": 20, "type": "Normal"},
            {"name": "Pikachu", "power": 25, "health": 100, "poison": 10, "heal": 20, "type": "Electric"},
            {"name": "Eevee", "power": 25, "health": 100, "poison": 10, "heal": 20, "type": "Normal"},
            {"name": "Charmander", "power": 30, "health": 100, "poison": 10, "heal": 20, "type": "Fire"},
            {"name": "Squirtle", "power": 30, "health": 100, "poison": 10, "heal": 20, "type": "Water"},
            {"name": "Bulbasaur", "power": 30, "health": 100, "poison": 10, "heal": 20, "type": "Grass"},
            {"name": "Gengar", "power": 35, "health": 100, "poison": 10, "heal": 20, "type": "Poison"},
            {"name": "Machamp", "power": 40, "health": 100, "poison": 10, "heal": 20, "type": "Fighting"},
            {"name": "Snorlax", "power": 40, "health": 100, "poison": 10, "heal": 20, "type": "Normal"},
            {"name": "Mewtwo", "power": 45, "health": 100, "poison": 10, "heal": 20, "type": "Psychic"}
], dtype=object) 
        p1 = []
        p2 = []
        battle = []
        battled_pokemon = set()
        battle_counter = 0
        grant = 5
        fatigue = 2

        print("\n(Pokemon name, Power, Health, Poison, Potion, Element)")
        for i, pokemon in enumerate(pokemon_data, start=1):
            print(f"{i}. {pokemon['name']}, {pokemon['power']}, {pokemon['health']}, {pokemon['poison']}, {pokemon['heal']}, {pokemon['type']}")

        while True:
            if len(p1) == 3 and len(p2) == 3:
                if len(battled_pokemon) < 6:
                    player1_index = rm.choice([i for i in range(3) if p1[i]['name'] not in battled_pokemon])
                    player2_index = rm.choice([i for i in range(3) if p2[i]['name'] not in battled_pokemon])
                    battle.append([p1[player1_index], p2[player2_index]])
                    battled_pokemon.add(p1[player1_index]["name"])  
                    battled_pokemon.add(p2[player2_index]["name"])   
                    battle_counter += 1
                    print(f"\nBattle {battle_counter}: {p1[player1_index]['name']} vs {p2[player2_index]['name']}")
                    
                    if p1[player1_index]["type"] in element[p2[player2_index]["type"]][0]:
                        print(f"{p1[player1_index]['name']} ({p1[player1_index]['type']}) is strong against {p2[player2_index]['name']} ({p2[player2_index]['type']})")
                        p2[player2_index]["power"] -= p1[player1_index]["poison"]
                        p1[player1_index]["poison"] = 0
                        p1[player1_index]["power"] += p1[player1_index]["heal"]
                        p1[player1_index]["heal"] = 0
                        print(f"{p2[player2_index]['name']} ({p2[player2_index]['type']}) is weak against {p1[player1_index]['name']} ({p1[player1_index]['type']})")
                        p1[player1_index]["power"] -= p2[player2_index]["poison"]
                        p2[player2_index]["poison"] = 0
                        p2[player2_index]["power"] += p2[player2_index]["heal"]
                        p2[player2_index]["heal"] = 0
                        if p1[player1_index]["power"] > p2[player2_index]["power"]:
                            p2[player2_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p1[player1_index]["health"] += grant
                            print(f"{p1[player1_index]['name']} wins!")
                        elif p1[player1_index]["power"] < p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p2[player2_index]["health"] += grant
                            print(f"{p2[player2_index]['name']} wins!")
                        elif p1[player1_index]["power"] == p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            print(f"Tie!")
                    elif p1[player1_index]["type"] in element[p2[player2_index]["type"]][1]:
                        print(f"{p2[player2_index]['name']} ({p2[player2_index]['type']}) is strong against {p1[player1_index]['name']} ({p1[player1_index]['type']})")
                        p1[player1_index]["power"] -= p2[player2_index]["poison"]
                        p2[player2_index]["poison"] = 0
                        p2[player2_index]["power"] += p2[player2_index]["heal"]
                        p2[player2_index]["heal"] = 0
                        print(f"{p1[player1_index]['name']} ({p1[player1_index]['type']}) is weak against {p2[player2_index]['name']} ({p2[player2_index]['type']})")
                        p2[player2_index]["power"] -= p1[player1_index]["poison"]
                        p1[player1_index]["poison"] = 0
                        p1[player1_index]["power"] += p1[player1_index]["heal"]
                        p1[player1_index]["heal"] = 0
                        if p1[player1_index]["power"] > p2[player2_index]["power"]:
                            p2[player2_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p1[player1_index]["health"] += grant
                            print(f"{p1[player1_index]['name']} wins!")
                        elif p1[player1_index]["power"] < p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p2[player2_index]["health"] += grant
                            print(f"{p2[player2_index]['name']} wins!")
                        elif p1[player1_index]["power"] == p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            print(f"Tie!")
                    else:
                        print(f"{p1[player1_index]['name']} ({p1[player1_index]['type']}) is neutral against {p2[player2_index]['name']} ({p2[player2_index]['type']})")
                        actionp1 = input(f"Player 1, do you want to use 'poison' or 'potion' or 'pandp' for {p1[player1_index]['name']}? (Enter 'none' to skip): ").lower()
                        actionp2 = input(f"Player 2, do you want to use 'poison' or 'potion' or 'pandp' for {p2[player2_index]['name']}? (Enter 'none' to skip): ").lower()
                        
                        if actionp1 == "poison":
                            p2[player2_index]["power"] -= p1[player1_index]["poison"]
                            p1[player1_index]["poison"] = 0
                        elif actionp1 == "potion":
                            p1[player1_index]["power"] += p1[player1_index]["heal"]
                            p1[player1_index]["heal"] = 0
                        elif actionp1 == "pandp":
                            p2[player2_index]["power"] -= p1[player1_index]["poison"]
                            p1[player1_index]["poison"] = 0
                            p1[player1_index]["power"] += p1[player1_index]["heal"]
                            p1[player1_index]["heal"] = 0
                        else:
                            print("Wrong input!")
                        if actionp2 == "poison":
                            p1[player1_index]["power"] -= p2[player2_index]["poison"]
                            p2[player2_index]["poison"] = 0
                        elif actionp2 == "potion":
                            p2[player2_index]["power"] += p2[player2_index]["heal"]
                            p2[player2_index]["heal"] = 0
                        elif actionp2 == "pandp":
                            p1[player1_index]["power"] -= p2[player2_index]["poison"]
                            p2[player2_index]["poison"] = 0
                            p2[player2_index]["power"] += p2[player2_index]["heal"]
                            p2[player2_index]["heal"] = 0
                        else:
                            print("Wrong input!")
                        if p1[player1_index]["power"] > p2[player2_index]["power"]:
                            p2[player2_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p1[player1_index]["health"] += grant
                            print(f"{p1[player1_index]['name']} wins!")
                        elif p1[player1_index]["power"] < p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p2[player2_index]["health"] += grant
                            print(f"{p2[player2_index]['name']} wins!")
                        elif p1[player1_index]["power"] == p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            print(f"Tie!")
                            
                    print(f"Battle log:")
                    print(tabulate(battle, headers=["Player 1 Pokémon", "Player 2 Pokémon"], tablefmt="grid"))

                else:
                    print("All Pokémon have participated in a battle!")
                    break 

            elif len(p1) != 3:
                # selection = int(input(f"Choose your Pokémon, Player 1: ")) - 1
                selection = rm.choice([i for i in range(len(pokemon_data))])
                if selection in [0, 1, 2]:
                    p1.append(pokemon_data[selection])
                    pokemon_data = np.delete(pokemon_data, selection)
                    print(f"\nPlayer 1 selected: {[p['name'] for p in p1]}\n")
                    for i, pokemon in enumerate(pokemon_data, start=1):
                        print(f"{i}. {pokemon['name']}, {pokemon['power']}, {pokemon['health']}, {pokemon['poison']}, {pokemon['heal']}, {pokemon['type']}")

            elif len(p2) != 3:
                # selection = int(input(f"Choose your Pokémon, Player 2: ")) - 1
                selection = rm.choice([i for i in range(len(pokemon_data))])
                if selection in [0, 1, 2]:
                    p2.append(pokemon_data[selection])
                    pokemon_data = np.delete(pokemon_data, selection)
                    print(f"\nPlayer 2 selected: {[p['name'] for p in p2]}\n")
                    for i, pokemon in enumerate(pokemon_data, start=1):
                        print(f"{i}. {pokemon['name']}, {pokemon['power']}, {pokemon['health']}, {pokemon['poison']}, {pokemon['heal']}, {pokemon['type']}")

        print("\nBattle Summary:")
        print(f"Total battles fought: {battle_counter}")
    elif action == "pa":
        battle_counter = 0
        battle = []
        battled_pokemon = set()
        while True:
            if len(p1) == 3 and len(p2) == 3:
                if len(battled_pokemon) < 6:
                    player1_index = rm.choice([i for i in range(3) if p1[i]['name'] not in battled_pokemon])
                    player2_index = rm.choice([i for i in range(3) if p2[i]['name'] not in battled_pokemon])
                    battle.append([p1[player1_index], p2[player2_index]])
                    battled_pokemon.add(p1[player1_index]["name"])  
                    battled_pokemon.add(p2[player2_index]["name"])   
                    battle_counter += 1
                    print(f"\nBattle {battle_counter}: {p1[player1_index]['name']} vs {p2[player2_index]['name']}")
                    
                    if p1[player1_index]["type"] in element[p2[player2_index]["type"]][0]:
                        print(f"{p1[player1_index]['name']} ({p1[player1_index]['type']}) is strong against {p2[player2_index]['name']} ({p2[player2_index]['type']})")
                        p2[player2_index]["power"] -= p1[player1_index]["poison"]
                        p1[player1_index]["poison"] = 0
                        p1[player1_index]["power"] += p1[player1_index]["heal"]
                        p1[player1_index]["heal"] = 0
                        print(f"{p2[player2_index]['name']} ({p2[player2_index]['type']}) is weak against {p1[player1_index]['name']} ({p1[player1_index]['type']})")
                        p1[player1_index]["power"] -= p2[player2_index]["poison"]
                        p2[player2_index]["poison"] = 0
                        p2[player2_index]["power"] += p2[player2_index]["heal"]
                        p2[player2_index]["heal"] = 0
                        if p1[player1_index]["power"] > p2[player2_index]["power"]:
                            p2[player2_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p1[player1_index]["health"] += grant
                            print(f"{p1[player1_index]['name']} wins!")
                        elif p1[player1_index]["power"] < p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p2[player2_index]["health"] += grant
                            print(f"{p2[player2_index]['name']} wins!")
                        elif p1[player1_index]["power"] == p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            print(f"Tie!")
                    elif p1[player1_index]["type"] in element[p2[player2_index]["type"]][1]:
                        print(f"{p2[player2_index]['name']} ({p2[player2_index]['type']}) is strong against {p1[player1_index]['name']} ({p1[player1_index]['type']})")
                        p1[player1_index]["power"] -= p2[player2_index]["poison"]
                        p2[player2_index]["poison"] = 0
                        p2[player2_index]["power"] += p2[player2_index]["heal"]
                        p2[player2_index]["heal"] = 0
                        print(f"{p1[player1_index]['name']} ({p1[player1_index]['type']}) is weak against {p2[player2_index]['name']} ({p2[player2_index]['type']})")
                        p2[player2_index]["power"] -= p1[player1_index]["poison"]
                        p1[player1_index]["poison"] = 0
                        p1[player1_index]["power"] += p1[player1_index]["heal"]
                        p1[player1_index]["heal"] = 0
                        if p1[player1_index]["power"] > p2[player2_index]["power"]:
                            p2[player2_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p1[player1_index]["health"] += grant
                            print(f"{p1[player1_index]['name']} wins!")
                        elif p1[player1_index]["power"] < p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p2[player2_index]["health"] += grant
                            print(f"{p2[player2_index]['name']} wins!")
                        elif p1[player1_index]["power"] == p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            print(f"Tie!")
                    else:
                        print(f"{p1[player1_index]['name']} ({p1[player1_index]['type']}) is neutral against {p2[player2_index]['name']} ({p2[player2_index]['type']})")
                        actionp1 = input(f"Player 1, do you want to use 'poison' or 'potion' or 'pandp' for {p1[player1_index]['name']}? (Enter 'none' to skip): ").lower()
                        actionp2 = input(f"Player 2, do you want to use 'poison' or 'potion' or 'pandp' for {p2[player2_index]['name']}? (Enter 'none' to skip): ").lower()
                        
                        if actionp1 == "poison":
                            p2[player2_index]["power"] -= p1[player1_index]["poison"]
                            p1[player1_index]["poison"] = 0
                        elif actionp1 == "potion":
                            p1[player1_index]["power"] += p1[player1_index]["heal"]
                            p1[player1_index]["heal"] = 0
                        elif actionp1 == "pandp":
                            p2[player2_index]["power"] -= p1[player1_index]["poison"]
                            p1[player1_index]["poison"] = 0
                            p1[player1_index]["power"] += p1[player1_index]["heal"]
                            p1[player1_index]["heal"] = 0
                        else:
                            print("Wrong input!")
                        if actionp2 == "poison":
                            p1[player1_index]["power"] -= p2[player2_index]["poison"]
                            p2[player2_index]["poison"] = 0
                        elif actionp2 == "potion":
                            p2[player2_index]["power"] += p2[player2_index]["heal"]
                            p2[player2_index]["heal"] = 0
                        elif actionp2 == "pandp":
                            p1[player1_index]["power"] -= p2[player2_index]["poison"]
                            p2[player2_index]["poison"] = 0
                            p2[player2_index]["power"] += p2[player2_index]["heal"]
                            p2[player2_index]["heal"] = 0
                        else:
                            print("Wrong input!")
                        if p1[player1_index]["power"] > p2[player2_index]["power"]:
                            p2[player2_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p1[player1_index]["health"] += grant
                            print(f"{p1[player1_index]['name']} wins!")
                        elif p1[player1_index]["power"] < p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= 10
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            p2[player2_index]["health"] += grant
                            print(f"{p2[player2_index]['name']} wins!")
                        elif p1[player1_index]["power"] == p2[player2_index]["power"]:
                            p1[player1_index]["health"] -= fatigue
                            p2[player2_index]["health"] -= fatigue
                            print(f"Tie!")
                            
                    print(f"Battle log:")
                    print(tabulate(battle, headers=["Player 1 Pokémon", "Player 2 Pokémon"], tablefmt="grid"))

                else:
                    print("All Pokémon have participated in a battle!")
                    break 

            elif len(p1) != 3:
                # selection = int(input(f"Choose your Pokémon, Player 1: ")) - 1
                selection = rm.choice([i for i in range(len(pokemon_data))])
                if selection in [0, 1, 2]:
                    p1.append(pokemon_data[selection])
                    pokemon_data = np.delete(pokemon_data, selection)
                    print(f"\nPlayer 1 selected: {[p['name'] for p in p1]}\n")
                    for i, pokemon in enumerate(pokemon_data, start=1):
                        print(f"{i}. {pokemon['name']}, {pokemon['power']}, {pokemon['health']}, {pokemon['poison']}, {pokemon['heal']}, {pokemon['type']}")

            elif len(p2) != 3:
                # selection = int(input(f"Choose your Pokémon, Player 2: ")) - 1
                selection = rm.choice([i for i in range(len(pokemon_data))])
                if selection in [0, 1, 2]:
                    p2.append(pokemon_data[selection])
                    pokemon_data = np.delete(pokemon_data, selection)
                    print(f"\nPlayer 2 selected: {[p['name'] for p in p2]}\n")
                    for i, pokemon in enumerate(pokemon_data, start=1):
                        print(f"{i}. {pokemon['name']}, {pokemon['power']}, {pokemon['health']}, {pokemon['poison']}, {pokemon['heal']}, {pokemon['type']}")
                    
        print("\nBattle Summary:")
        print(f"Total battles fought: {battle_counter}")
    else:
        print(" Thankyou for playing!")
        exit()





'''
import numpy as np
import random as rm
from tabulate import tabulate

# Define Pokémon data structure and initialize Pokémon list
list_dtype = [("name", "U16"), ("power", "i8"), ("health", "i8"), ("poison", "i8"), ("heal", "i8"), ("type", "U16")]
pokemon_array = np.array([
    ("Jigglypuff", 25, 100, 10, 20, "Normal"), 
    ("Pikachu", 25, 100, 10, 20, "Electric"),
    ("Eevee", 25, 100, 10, 20, "Normal"), 
    ("Charmander", 30, 100, 10, 20, "Fire"),
    ("Squirtle", 30, 100, 10, 20, "Water"),
    ("Bulbasaur", 30, 100, 10, 20, "Grass"), 
    ("Gengar", 35, 100, 10, 20, "Poison"),
    ("Machamp", 40, 100, 10, 20, "Fighting"),
    ("Snorlax", 40, 100, 10, 20, "Normal"), 
    ("Mewtwo", 45, 100, 10, 20, "Psychic")
], dtype=list_dtype)

# Dictionary for Pokémon type advantages and disadvantages
element = {
    "Electric": [["Water"], ["None"]],
    "Fire": [["Grass"], ["Water", "Fire"]],
    "Water": [["Fire"], ["Electric", "Grass"]],
    "Normal": [["None"], ["None"]],
    "Fighting": [["Normal"], ["Psychic"]],
    "Psychic": [["Fighting"], ["None"]],
    "Grass": [["Water"], ["Fire"]],
    "Poison": [["Grass"], ["Poison", "Psychic"]],
}

# Player selections and battle logs
p1 = []
p2 = []
duel = []
battled_pokemon = set()  
battle_counter = 0 

def display():
    print("\nAvailable Pokémon:")
    for i in range(len(pokemon_array)):
        print(f"{i+1}. {pokemon_array[i]}")

def select_pokemon(player_num, selected_list):
    global pokemon_array
    display()
    # selection = int(input(f"Choose your Pokémon, Player {player_num}: ")) - 1
    selection = 0  # Replace with user input in practical use
    if str(selection).isdigit() and int(selection) in range(len(pokemon_array)):
        selected_list.append(pokemon_array[int(selection)].tolist())
        pokemon_array = np.delete(pokemon_array, int(selection))
        print(f"\nPlayer {player_num} selected: {selected_list[-1]}\n")
        if p1:
            print(tabulate(p1, headers=["Player 1 Pokémon", "Damage", "Health", "Poison", "Potion", "Element"], tablefmt="grid"))
        if p2:
            print(tabulate(p2, headers=["Player 2 Pokémon", "Damage", "Health", "Poison", "Potion", "Element"], tablefmt="grid"))
    else:
        print("Invalid input, try again.")

def determine_strength(attacker_type, defender_type):
    if defender_type in element[attacker_type][0]:
        return "strong"
    elif defender_type in element[attacker_type][1]:
        return "weak"
    else:
        return "neutral"

def apply_poison_or_potion(selected_pokemon, action):
    # Convert selected_pokemon to a list to allow modifications
    selected_pokemon_list = list(selected_pokemon)

    if action == "poison":
        selected_pokemon_list[2] -= selected_pokemon_list[3]  # Reduce health by poison amount
        print(f"{selected_pokemon_list[0]} was poisoned! Health reduced by {selected_pokemon_list[3]}. New health: {selected_pokemon_list[2]}")
    elif action == "potion":
        selected_pokemon_list[2] += selected_pokemon_list[4]  # Increase health by potion amount
        print(f"{selected_pokemon_list[0]} used a potion! Health restored by {selected_pokemon_list[4]}. New health: {selected_pokemon_list[2]}")

    # Update the Pokémon in the player's list (p1 or p2)
    # if selected_pokemon in p1:
    #     p1[p1.index(selected_pokemon)] = tuple(selected_pokemon_list)
    # elif selected_pokemon in p2:
    #     p2[p2.index(selected_pokemon)] = tuple(selected_pokemon_list)


def battle():
    global battle_counter
    if len(battled_pokemon) < 6:
        # Choose Pokémon for each player and convert to lists for mutability
        arnma = list(rm.choice(p1))
        dmps = list(rm.choice(p2))

        battle_counter += 1
        
        # Determine strength relation
        arnma_type = arnma[5]
        dmps_type = dmps[5]
        arnma_strength = determine_strength(arnma_type, dmps_type)
        dmps_strength = determine_strength(dmps_type, arnma_type)
        
        print(f"\nBattle {battle_counter}: {arnma[0]} vs {dmps[0]}")
        print(f"{arnma[0]} is {arnma_strength} against {dmps[0]} ({arnma_type} vs {dmps_type})")
        print(f"{dmps[0]} is {dmps_strength} against {arnma[0]} ({dmps_type} vs {arnma_type})")
        
        # If neutral, ask both players if they want to use poison or potion
        if arnma_strength == "neutral" and dmps_strength == "neutral":
            for pokemon, player_num in [(arnma, 1), (dmps, 2)]:
                action = input(f"Player {player_num}, do you want to use 'poison' or 'potion' for {pokemon[0]}? (Enter 'none' to skip): ").lower()
                if action in ["poison", "potion"]:
                    apply_poison_or_potion(pokemon, action)
        
        # After any modifications, add the updated Pokémon to the duel log
        duel.append([arnma[:], dmps[:]])  # Use slicing to copy the modified lists
        print(duel[0][2])
        print("Battle log:")
        print(tabulate(duel, headers=["Player 1 Pokémon", "Player 2 Pokémon"], tablefmt="grid"))

    else:
        print("All Pokémon have participated in a battle!")  
 
      

def play_game():
    while True:
        if len(p1) == 3 and len(p2) == 3:
            battle()
            if len(battled_pokemon) >= 6:
                break
        elif len(p1) != 3:
            select_pokemon(1, p1)
        elif len(p2) != 3:
            select_pokemon(2, p2)

    print("\nBattle Summary:")
    print(f"Total battles fought: {battle_counter}")

# Start the game
play_game()
'''

'''
pdf accurate
import random

# Updated Pokémon data: (name, power, health, poison damage, potion healing, type)
pokemon_data = [
    ("Jigglypuff", 25, 100, 10, 20, "Normal"), 
    ("Pikachu", 25, 100, 10, 20, "Electric"),
    ("Eevee", 25, 100, 10, 20, "Normal"), 
    ("Charmander", 30, 100, 10, 20, "Fire"),
    ("Squirtle", 30, 100, 10, 20, "Water"),
    ("Bulbasaur", 30, 100, 10, 20, "Grass"), 
    ("Gengar", 35, 100, 10, 20, "Ghost"),
    ("Machamp", 40, 100, 10, 20, "Fighting"),
    ("Snorlax", 40, 100, 10, 20, "Normal"), 
    ("Mewtwo", 45, 100, 10, 20, "Psychic")
]

# Player selections
player1_pokemon = []
player2_pokemon = []
player1_wins = 0
player2_wins = 0

# Function to print Pokémon list
def print_pokemon_list():
    print("Available Pokémon:")
    for i, (name, power, health, poison, potion, p_type) in enumerate(pokemon_data):
        print(f"{i+1}: {name} (Type: {p_type}, Power: {power}, Health: {health})")

# Player selection process
def select_pokemon(player_num, player_pokemon):
    while len(player_pokemon) < 3:
        print_pokemon_list()
        # choice = 0
        choice = int(input(f"Player {player_num}, select your Pokémon by number: ")) - 1
        if 0 <= choice < len(pokemon_data):
            player_pokemon.append(pokemon_data.pop(choice))
        else:
            print("Invalid selection. Try again.")

# Simulate a single battle
def battle(pokemon1, pokemon2):
    global player1_wins, player2_wins

    name1, power1, health1, poison1, potion1, type1 = pokemon1
    name2, power2, health2, poison2, potion2, type2 = pokemon2

    print(f"\n{name1} (Player 1) VS {name2} (Player 2)")
    print(f"{name1} attacks {name2} with {type1} power!")
    print(f"{name2} retaliates with a {type2}-type attack!")

    # Determine the winner based on power
    if power1 > power2:
        print(f"{name1} lands a critical hit! {name2} is knocked back!")
        print(f"{name1} wins the battle!")
        health1 += 5  # Health increase for winner
        health2 -= 10  # Health decrease for loser
        player1_wins += 1
    elif power2 > power1:
        print(f"{name2} counters the attack! {name1} is struggling to stay in the fight!")
        print(f"{name2} wins the battle!")
        health2 += 5
        health1 -= 10
        player2_wins += 1
    else:
        print("Both Pokémon are equally matched! It's a tie!")

    # Fatigue
    health1 -= 2
    health2 -= 2
    print(f"Both Pokémon are fatigued from the battle, losing 2 health points each.")

    # Apply poison and potion effects
    print(f"{name1} takes {poison1} poison damage but uses a potion to heal {potion1}!")
    print(f"{name2} takes {poison2} poison damage but uses a potion to heal {potion2}!")
    
    health1 -= poison1
    health2 -= poison2
    health1 += potion1
    health2 += potion2

    # Clamp health values to be between 0 and 100
    health1 = max(0, min(health1, 100))
    health2 = max(0, min(health2, 100))

    print(f"{name1}'s health is now {health1}.")
    print(f"{name2}'s health is now {health2}.\n")

    # Update Pokémon health in player arrays
    pokemon1 = (name1, power1, health1, poison1, potion1, type1)
    pokemon2 = (name2, power2, health2, poison2, potion2, type2)

    return pokemon1, pokemon2

# Function to simulate the entire battle sequence
def battle_sequence():
    for i in range(3):  # Three rounds
        print(f"\n--- Round {i+1} ---")
        for p1, p2 in zip(player1_pokemon, player2_pokemon):
            # Simulate battle and update Pokémon stats
            p1, p2 = battle(p1, p2)

# Function to declare the overall winner
def declare_winner():
    print("\n--- Final Results ---")
    print(f"Player 1 Wins: {player1_wins}")
    print(f"Player 2 Wins: {player2_wins}")
    
    if player1_wins > player2_wins:
        print("Player 1 is the overall winner!")
    elif player2_wins > player1_wins:
        print("Player 2 is the overall winner!")
    else:
        print("It's a tie!")

# Main game flow
def main():
    print("Welcome to Pokémon Battle Royale: Power, Strategy, and Fatigue!")

    # Player 1 selects Pokémon
    select_pokemon(1, player1_pokemon)
    
    # Player 2 selects Pokémon
    select_pokemon(2, player2_pokemon)
    
    # Battle simulation
    battle_sequence()

    # Declare the winner
    declare_winner()

# Start the game
if __name__ == "__main__":
    main()'''

"""
this is for element diff

f arnma[5] in element:
            strong = element[arnma[5]][0]
            weak = element[arnma[5]][1]
            if dmps[5] in strong:
                print(f"{arnma[5]} is strong against {dmps[5]}.")
            elif dmps[5] in weak:
                print(f"{arnma[5]} is weak against {dmps[5]}.")

or or or or or or or or or or or or or or or or or or or or or or or or or or

if p1[arnma][5] in element:
                strong = element[p1[arnma][5]][0]
                weak = element[p1[arnma][5]][1]
                if p2[dmps][5] in strong:
                    print(f"{p1[arnma][5]} is strong against {p2[dmps][5]}.")
                elif p2[dmps][5] in weak:
                    print(f"{p1[arnma][5]} is weak against {p2[dmps][5]}.")

"""
