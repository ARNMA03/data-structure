import numpy as np
import random as rm
from tabulate import tabulate

def pokemon_data():
    return np.array([
        {"name": "Jigglypuff", "power": 31, "health": 100, "poison": 10, "heal": 20, "type": "Normal"},
        {"name": "Pikachu", "power": 23, "health": 100, "poison": 10, "heal": 20, "type": "Electric"},
        {"name": "Eevee", "power": 34,"health": 100, "poison": 10,"heal": 20, "type": "Normal"},
        {"name": "Charmander", "power": 28,"health": 100, "poison": 10,"heal": 20, "type": "Fire"},
        {"name": "Squirtle", "power": 32, "health": 100, "poison": 10, "heal": 20, "type": "Water"},
        {"name": "Bulbasaur", "power": 29, "health": 100, "poison": 10, "heal": 20, "type": "Grass"},
        {"name": "Gengar", "power": 27, "health": 100, "poison": 10, "heal": 20, "type": "Poison"},
        {"name": "Machamp", "power": 26, "health": 100, "poison": 10, "heal": 20, "type": "Fighting"},
        {"name": "Snorlax", "power": 21, "health": 100, "poison": 10, "heal": 20, "type": "Normal"},
        {"name": "Mewtwo", "power": 25, "health": 100, "poison": 10, "heal": 20, "type": "Psychic"}
    ], dtype=object)

def elementtypes():
    return {
        "Electric": [["Water"], ["None"]],
        "Fire": [["Grass"], ["Water", "Fire"]],
        "Water": [["Fire"], ["Electric", "Grass"]],
        "Normal": [["None"], ["None"]],
        "Fighting": [["Normal"], ["Psychic"]],
        "Psychic": [["Fighting"], ["None"]],
        "Grass": [["Water"], ["Fire"]],
        "Poison": [["Grass"], ["Poison", "Psychic"]]
    }

def resetgame(team_size=3):
    return {
        'pokemon_data': pokemon_data(),
        'p1': [],
        'p2': [],
        'battle': [],
        'battled_pokemon': set(),
        'battle_counter': 0,
        'grant': 5,
        'fatigue': 2,
        'team_size': team_size
    }

def pokemonlist(pokemon_data):
    print("\n(Pokemon name, Power, Health, Poison, Potion, Element)")
    for i, pokemon in enumerate(pokemon_data, start=1):
        print(f"{i}. {pokemon['name']}, {pokemon['power']}, {pokemon['health']}, {pokemon['poison']}, {pokemon['heal']}, {pokemon['type']}")

def pokemonselection(pokemon_data, player_pokemon, player_name, team_size):
    pokemonlist(pokemon_data)
    
    max_pokemon = len(pokemon_data)
    remaining_slots = team_size - len(player_pokemon)
    
    try:
        choice = int(input(f"Choose your Pokémon, {player_name} (1-{max_pokemon}): "))
        
        if 1 <= choice <= max_pokemon:
            selected_pokemon = pokemon_data[choice - 1].copy()
            pokemon_data = np.delete(pokemon_data, choice - 1)
            player_pokemon.append(selected_pokemon)
            print(f"\n{player_name} selected: {[p['name'] for p in player_pokemon]}")
            print(f"Remaining slots: {remaining_slots - 1}\n")
            
            return pokemon_data
        else:
            print(f"\nError: Please choose a number between 1 and {max_pokemon}!")
            return pokemonselection(pokemon_data, player_pokemon, player_name, team_size)
    except ValueError:
        print("\nError: Please enter a number!")
        return pokemonselection(pokemon_data, player_pokemon, player_name, team_size)

def processactions(p1_pokemon, p2_pokemon, name1, name2):
    # Show current stats before asking for actions
    print(f"\nCurrent Stats:")
    print(f"{name1}'s {p1_pokemon['name']}: Power={p1_pokemon['power']}, Poison={p1_pokemon['poison']}, Heal={p1_pokemon['heal']}")
    print(f"{name2}'s {p2_pokemon['name']}: Power={p2_pokemon['power']}, Poison={p2_pokemon['poison']}, Heal={p2_pokemon['heal']}")
    
    # Check if actions would be meaningful
    p1_can_act = p1_pokemon['poison'] > 0 or p1_pokemon['heal'] > 0
    p2_can_act = p2_pokemon['poison'] > 0 or p2_pokemon['heal'] > 0
    
    if not p1_can_act and not p2_can_act:
        print("\nBoth players have used all their items!")
        return
        
    if p1_can_act:
        actionp1 = input(f"{name1}, do you want to use 'poison' or 'potion' or 'pandp'(both) for {p1_pokemon['name']}? (Enter 'none' to skip): ").lower()
        if actionp1 == "poison" and p1_pokemon['poison'] > 0:
            p2_pokemon["power"] -= p1_pokemon["poison"]
            p1_pokemon["poison"] = 0
            print(f"{name1} used poison! {name2}'s {p2_pokemon['name']}'s power reduced to {p2_pokemon['power']}")
        elif actionp1 == "potion" and p1_pokemon['heal'] > 0:
            p1_pokemon["power"] += p1_pokemon["heal"]
            p1_pokemon["heal"] = 0
            print(f"{name1} used potion! {p1_pokemon['name']}'s power increased to {p1_pokemon['power']}")
        elif actionp1 == "pandp" and p1_pokemon['poison'] > 0 and p1_pokemon['heal'] > 0:
            p2_pokemon["power"] -= p1_pokemon["poison"]
            p1_pokemon["poison"] = 0
            p1_pokemon["power"] += p1_pokemon["heal"]
            p1_pokemon["heal"] = 0
            print(f"{name1} used both! {p1_pokemon['name']}'s power = {p1_pokemon['power']}, {name2}'s {p2_pokemon['name']}'s power = {p2_pokemon['power']}")
        elif actionp1 == "none":
            print(f"{name1} skipped their action")
        else:
            print("Invalid input or no items available!")
    else:
        print(f"{name1}'s {p1_pokemon['name']} has no items left to use!")
    
    if p2_can_act:
        actionp2 = input(f"{name2}, do you want to use 'poison' or 'potion' or 'pandp'(both) for {p2_pokemon['name']}? (Enter 'none' to skip): ").lower()
        if actionp2 == "poison" and p2_pokemon['poison'] > 0:
            p1_pokemon["power"] -= p2_pokemon["poison"]
            p2_pokemon["poison"] = 0
            print(f"{name2} used poison! {name1}'s {p1_pokemon['name']}'s power reduced to {p1_pokemon['power']}")
        elif actionp2 == "potion" and p2_pokemon['heal'] > 0:
            p2_pokemon["power"] += p2_pokemon["heal"]
            p2_pokemon["heal"] = 0
            print(f"{name2} used potion! {p2_pokemon['name']}'s power increased to {p2_pokemon['power']}")
        elif actionp2 == "pandp" and p2_pokemon['poison'] > 0 and p2_pokemon['heal'] > 0:
            p1_pokemon["power"] -= p2_pokemon["poison"]
            p2_pokemon["poison"] = 0
            p2_pokemon["power"] += p2_pokemon["heal"]
            p2_pokemon["heal"] = 0
            print(f"{name2} used both! {p2_pokemon['name']}'s power = {p2_pokemon['power']}, {name1}'s {p1_pokemon['name']}'s power = {p1_pokemon['power']}")
        elif actionp2 == "none":
            print(f"{name2} skipped their action")
        else:
            print("Invalid input or no items available!")
    else:
        print(f"{name2}'s {p2_pokemon['name']} has no items left to use!")
    
    print("\nFinal Stats after actions:")
    print(f"{name1}'s {p1_pokemon['name']}: Power={p1_pokemon['power']}, Poison={p1_pokemon['poison']}, Heal={p1_pokemon['heal']}")
    print(f"{name2}'s {p2_pokemon['name']}: Power={p2_pokemon['power']}, Poison={p2_pokemon['poison']}, Heal={p2_pokemon['heal']}")

def calculate_battle_outcome(p1_pokemon, p2_pokemon, grant, fatigue):
    # Calculate battle outcome
    if p1_pokemon["power"] > p2_pokemon["power"]:
        # P1 wins: P2 takes damage, P1 gets grant, both get fatigue
        p2_pokemon["health"] -= 10  # Damage
        p1_pokemon["health"] += grant  # Winner bonus
        p1_pokemon["health"] -= fatigue  # Fatigue
        p2_pokemon["health"] -= fatigue  # Fatigue
        
        print(f"\nAfter battle:")
        print(f"{p1_pokemon['name']} wins!")
        print(f"- {p2_pokemon['name']} takes 10 damage")
        print(f"- {p1_pokemon['name']} gets {grant} HP (grant)")
        print(f"- Both pokemon lose {fatigue} HP (fatigue)")
        
        if p1_pokemon["health"] <= 0 or p2_pokemon["health"] <= 0:
            return "exit"
            
        return f"{p1_pokemon['name']} wins!"
        
    elif p1_pokemon["power"] < p2_pokemon["power"]:
        # P2 wins: P1 takes damage, P2 gets grant, both get fatigue
        p1_pokemon["health"] -= 10  # Damage
        p2_pokemon["health"] += grant  # Winner bonus
        p1_pokemon["health"] -= fatigue  # Fatigue
        p2_pokemon["health"] -= fatigue  # Fatigue
        
        print(f"\nAfter battle:")
        print(f"{p2_pokemon['name']} wins!")
        print(f"- {p1_pokemon['name']} takes 10 damage")
        print(f"- {p2_pokemon['name']} gets {grant} HP (grant)")
        print(f"- Both pokemon lose {fatigue} HP (fatigue)")
        
        if p1_pokemon["health"] <= 0 or p2_pokemon["health"] <= 0:
            return "exit"
            
        return f"{p2_pokemon['name']} wins!"
        
    else:
        # Tie: both get fatigue only
        p1_pokemon["health"] -= fatigue
        p2_pokemon["health"] -= fatigue
        
        print(f"\nAfter battle:")
        print(f"Tie!")
        print(f"- Both pokemon lose {fatigue} HP (fatigue)")
        
        if p1_pokemon["health"] <= 0 or p2_pokemon["health"] <= 0:
            return "exit"
            
        return "Tie!"

def display_battle_log(game_state):
    headers = ["Round", "Player 1", "Player 2", "Result"]
    table_data = []
    
    for battle in game_state['battle']:
        table_data.append([
            f"Battle {battle['round']}", 
            f"{battle['p1_name']} (HP:{battle['p1_health']}, PWR:{battle['p1_power']}, PSN:{battle['p1_poison']}, HEL:{battle['p1_heal']})",
            f"{battle['p2_name']} (HP:{battle['p2_health']}, PWR:{battle['p2_power']}, PSN:{battle['p2_poison']}, HEL:{battle['p2_heal']})",
            battle['status']
        ])
    
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def conduct_battle_round(game_state, element):
    available_p1 = [p for p in game_state['p1'] if p['name'] not in game_state['battled_pokemon']]
    available_p2 = [p for p in game_state['p2'] if p['name'] not in game_state['battled_pokemon']]
    
    if available_p1 and available_p2:
        p1_pokemon = available_p1[0]
        p2_pokemon = available_p2[0]
        name1 = game_state['player_names'][1]
        name2 = game_state['player_names'][2]
        
        # Battle display and logic using direct Pokemon properties
        print(f"\nBattle {game_state['battle_counter'] + 1}: {name1}'s {p1_pokemon['name']} vs {name2}'s {p2_pokemon['name']}")
        
        print("\nCurrent Stats:")
        print(f"{name1}'s {p1_pokemon['name']}: Power={p1_pokemon['power']}, Poison={p1_pokemon['poison']}, Heal={p1_pokemon['heal']}")
        print(f"{name2}'s {p2_pokemon['name']}: Power={p2_pokemon['power']}, Poison={p2_pokemon['poison']}, Heal={p2_pokemon['heal']}")
        
        # Process player actions
        processactions(p1_pokemon, p2_pokemon, name1, name2)
        
        # Calculate battle outcome
        battle_result = calculate_battle_outcome(p1_pokemon, p2_pokemon, game_state['grant'], game_state['fatigue'])
        
        # Check if any Pokemon fainted during battle
        if p1_pokemon['health'] <= 0 or p2_pokemon['health'] <= 0:
            fainted = p1_pokemon['name'] if p1_pokemon['health'] <= 0 else p2_pokemon['name']
            winner = p2_pokemon['name'] if p1_pokemon['health'] <= 0 else p1_pokemon['name']
            battle_result = f"{fainted} fainted! {winner} wins!"
        
        # Create battle entry
        battle_entry = {
            'round': game_state['battle_counter'] + 1,
            'p1_name': p1_pokemon['name'],
            'p2_name': p2_pokemon['name'],
            'p1_health': p1_pokemon['health'],
            'p2_health': p2_pokemon['health'],
            'p1_power': p1_pokemon['power'],
            'p2_power': p2_pokemon['power'],
            'p1_poison': p1_pokemon.get('poison', 0),
            'p2_poison': p2_pokemon.get('poison', 0),
            'p1_heal': p1_pokemon.get('heal', 0),
            'p2_heal': p2_pokemon.get('heal', 0),
            'status': battle_result
        }
        
        # Add battle to history
        game_state['battle'].append(battle_entry)
        game_state['battled_pokemon'].add(p1_pokemon['name'])
        game_state['battled_pokemon'].add(p2_pokemon['name'])
        game_state['battle_counter'] += 1
        
        # Display battle log
        print("\nBattle Log:")
        headers = ["Round", name1, name2, "Result"]
        table_data = [[
            f"Battle {b['round']}", 
            f"{b['p1_name']} (HP:{b['p1_health']}, PWR:{b['p1_power']}, PSN:{b['p1_poison']}, HEL:{b['p1_heal']})", 
            f"{b['p2_name']} (HP:{b['p2_health']}, PWR:{b['p2_power']}, PSN:{b['p2_poison']}, HEL:{b['p2_heal']})",
            b['status']
        ] for b in game_state['battle']]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print()
        
        # End game if a Pokemon has fainted
        if p1_pokemon['health'] <= 0 or p2_pokemon['health'] <= 0:
            print(f"\n{battle_result}")
            print("Game ended due to Pokemon fainting!")
            display_battle_summary(game_state)
            return False
            
        return True
    else:
        print("All Pokémon have participated in a battle!")
        return False

def resetbattle(gamestate):
    gamestate['battle'] = []
    gamestate['battled_pokemon'] = set()
    gamestate['battle_counter'] = 0
    return gamestate

def display_battle_summary(game_state):
    print("\n=== BATTLE SUMMARY ===")
    print(f"Total battles fought: {game_state['battle_counter']}")
    
    p1_total_health = sum(pokemon['health'] for pokemon in game_state['p1'])
    p2_total_health = sum(pokemon['health'] for pokemon in game_state['p2'])
    
    print("\nPlayer 1 Pokemon Status:")
    for pokemon in game_state['p1']:
        print(f"{pokemon['name']}: Health={pokemon['health']}, Power={pokemon['power']}")
    print(f"Total Team Health: {p1_total_health}")
    
    print("\nPlayer 2 Pokemon Status:")
    for pokemon in game_state['p2']:
        print(f"{pokemon['name']}: Health={pokemon['health']}, Power={pokemon['power']}")
    print(f"Total Team Health: {p2_total_health}")
    
    print("\nTeam Health Comparison:")
    if p1_total_health > p2_total_health:
        print(f"Player 1 leads by {p1_total_health - p2_total_health} health points!")
    elif p2_total_health > p1_total_health:
        print(f"Player 2 leads by {p2_total_health - p1_total_health} health points!")
    else:
        print("Both teams have equal total health!")
    
    print("\nBattle History:")
    for battle in game_state['battle']:
        print(f"Round {battle['round']}: {battle['p1_name']} vs {battle['p2_name']} - {battle['status']}")
    print("==================\n")

def coin_toss():
    print("\n=== PLAYER NAMES ===")
    p1_name = input("Enter Player 1's name: ").strip()
    p2_name = input("Enter Player 2's name: ").strip()
    
    print("\n=== COIN TOSS ===")
    # Get the call before the flip
    call = input(f"{p1_name}, call Heads or Tails: ").capitalize()
    while call not in ['Heads', 'Tails']:
        print("Please enter either 'Heads' or 'Tails'!")
        call = input(f"{p1_name}, call Heads or Tails: ").capitalize()
    
    print(f"\n{p1_name} called: {call}")
    input(f"Press Enter to flip the coin...")
    
    # Use random.choice with equal probability
    result = rm.choice(['Heads', 'Tails'])
    print(f"\nThe coin shows: {result}!")
    
    # Determine winner
    if call == result:
        first_player = 1
        first_player_name = p1_name
        print(f"\n{p1_name} called it right!")
    else:
        first_player = 2
        first_player_name = p2_name
        print(f"\n{p1_name} called it wrong!")
    
    print(f"{first_player_name} will pick first and have the rights to choose the team size!")
    
    return first_player, p1_name, p2_name

def playgame(gamestate, element, newgame=True, skip_names=False):
    if newgame and not skip_names:
        print("\n=== PLAYER NAMES ===")
        gamestate['player_names'] = {
            1: input("Enter Player 1's name: "),
            2: input("Enter Player 2's name: ")
        }
    
    # Initialize or reset battle-related fields
    if newgame:
        gamestate['p1'] = []
        gamestate['p2'] = []
        gamestate['battle'] = []
        gamestate['battled_pokemon'] = set()
        gamestate['battle_counter'] = 0
    
    # Pokemon selection for new game
    if newgame:
        print(f"\nEach player will select {gamestate['team_size']} Pokemon!")
        
        # Alternate selections between players
        for i in range(gamestate['team_size'] * 2):  # Total selections needed
            current_player = 1 if i % 2 == 0 else 2  # Alternate between 1 and 2
            player_list = gamestate['p1'] if current_player == 1 else gamestate['p2']
            player_name = gamestate['player_names'][current_player]
            
            print(f"\n{player_name}, select your Pokemon! ({len(player_list)}/{gamestate['team_size']})")
            
            # Show current teams after each selection
            if i > 0:
                print("\nCurrent Teams:")
                if len(gamestate['p1']) > 0:
                    print(f"{gamestate['player_names'][1]}: {[p['name'] for p in gamestate['p1']]}")
                if len(gamestate['p2']) > 0:
                    print(f"{gamestate['player_names'][2]}: {[p['name'] for p in gamestate['p2']]}")
                print()
            
            gamestate['pokemon_data'] = pokemonselection(
                gamestate['pokemon_data'], 
                player_list, 
                player_name, 
                gamestate['team_size']
            )
    
    # Battle continues until all Pokemon have battled
    battle_continues = True
    while battle_continues:
        battle_continues = conduct_battle_round(gamestate, element)
    
    return gamestate

def gamehistory():
    return {
        'games_played': 0,
        'history': [],
        'current_game': None
    }

def addtohistory(history, game_state):
    if game_state is None or 'p1' not in game_state or 'p2' not in game_state:
        print("Warning: Invalid game state")
        return history
        
    history['games_played'] += 1
    try:
        p1_health = sum(p['health'] for p in game_state['p1'])
        p2_health = sum(p['health'] for p in game_state['p2'])
        
        game_data = {
            'game_number': history['games_played'],
            'p1_health': p1_health,
            'p2_health': p2_health,
            'p1_team': [{'name': p['name'], 'type': p['type']} for p in game_state['p1']],
            'p2_team': [{'name': p['name'], 'type': p['type']} for p in game_state['p2']],
            'battles': game_state['battle'].copy() if 'battle' in game_state else [],
            'status': 'Player 1 won' if p1_health > p2_health else 'Player 2 won' if p2_health > p1_health else 'Draw'
        }
        
        history['history'].append(game_data)
        history['current_game'] = game_data
        
    except Exception as e:
        print(f"Warning: Error processing game history - {str(e)}")
    
    return history

def displayhistory(history):
    print("\n\n=== OVERALL GAME HISTORY ===")
    headers = ["Game", "Team 1", "P1 Health", "Team 2", "P2 Health", "Status"]
    table_data = []
    for game in history['history']:
        p1_team = ", ".join([p['name'] for p in game['p1_team']])
        p2_team = ", ".join([p['name'] for p in game['p2_team']])
        table_data.append([
            f"Game {game['game_number']}", 
            p1_team,
            game['p1_health'], 
            p2_team,
            game['p2_health'], 
            game['status']
        ])
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
    print("\n=== TEAM MATCHUP STATISTICS ===")
    matchups = {}
    for game in history['history']:
        p1_team = tuple(sorted([p['name'] for p in game['p1_team']]))
        p2_team = tuple(sorted([p['name'] for p in game['p2_team']]))
        matchup_key = (p1_team, p2_team)
        if matchup_key not in matchups:
            matchups[matchup_key] = {
                'total': 0,
                'p1_wins': 0,
                'p2_wins': 0,
                'draws': 0
            }
        matchups[matchup_key]['total'] += 1
        if game['status'] == 'Player 1 won':
            matchups[matchup_key]['p1_wins'] += 1
        elif game['status'] == 'Player 2 won':
            matchups[matchup_key]['p2_wins'] += 1
        else:
            matchups[matchup_key]['draws'] += 1
    headers = ["Team 1", "Team 2", "Total Games", "P1 Wins", "P2 Wins", "Draws"]
    table_data = []
    for (p1_team, p2_team), stats in matchups.items():
        table_data.append([
            ", ".join(p1_team),
            ", ".join(p2_team),
            stats['total'],
            stats['p1_wins'],
            stats['p2_wins'],
            stats['draws']
        ])
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def mainloop():
    gamestate = resetgame()
    element = elementtypes()
    history = gamehistory()
    
    while True:
        # Check for fainted Pokemon
        any_fainted = False
        fainted_pokemon = []
        
        if len(gamestate['p1']) > 0 and len(gamestate['p2']) > 0:
            for pokemon in gamestate['p1'] + gamestate['p2']:
                if pokemon['health'] <= 0:  # Simplified check
                    any_fainted = True
                    fainted_pokemon.append(pokemon['name'])
        
        # Show menu
        if any_fainted:
            print("\nSome Pokemon have fainted:", ", ".join(fainted_pokemon))
            displayhistory(history)
            print("\n'png' to Play New Game(New character) or")
            print("any character to exit")
        else:
            print("\n'png' to Play New Game(New character) or")
            print("'pa' to Play Again(Same set of characters) or")
            print("any character to exit")
            
        action = input("type the letter of the operation you want to do: ").lower().strip()
        
        if action in ['png', 'pa']:
            if any_fainted and action == "pa":
                print("\nCannot continue with fainted Pokemon. Please start a new game.")
                continue
            
            if action == "pa" and len(gamestate['p1']) == 0:
                print("\nNo Pokemon selected. Starting new game instead...")
                action = "png"
            
            if action == "png":
                # Get player names first
                print("\n=== PLAYER NAMES ===")
                name1 = input("Enter Player 1's name: ")
                name2 = input("Enter Player 2's name: ")
                
                # Do coin toss
                print("\n=== COIN TOSS ===")
                while True:
                    call = input(f"{name1}, call Heads or Tails: ").lower()
                    if call in ['heads', 'tails']:
                        break
                    print("Please enter either 'Heads' or 'Tails'!")
                
                print(f"\n{name1} called: {call.capitalize()}")
                input("Press Enter to flip the coin...")
                
                result = "heads" if rm.random() < 0.5 else "tails"
                print(f"\nThe coin shows: {result.capitalize()}!")
                
                # Determine winner of coin toss
                coin_winner = name1 if call == result else name2
                coin_loser = name2 if call == result else name1
                print(f"\n{coin_winner} {'called it right' if call == result else 'wins the toss'}!")
                print(f"{coin_winner} will pick first!")
                
                # Winner chooses team size
                print(f"\n=== TEAM SIZE ===")
                while True:
                    size_input = input(f"{coin_winner}, choose team size (3 or 4 Pokemon per team): ").strip()
                    if size_input in ['3', '4']:
                        current_team_size = int(size_input)
                        print(f"\nEach player will select {current_team_size} Pokemon!")
                        break
                    print("Please enter either 3 or 4!")
                
                # Set up game with winner going first
                gamestate = resetgame(current_team_size)
                # Store player names in gamestate
                gamestate['player_names'] = {
                    1: coin_winner,  # Winner goes first
                    2: coin_loser    # Loser goes second
                }
                
                # Pass newgame=True and skip_names=True
                gamestate = playgame(gamestate, element, newgame=True, skip_names=True)
                history = addtohistory(history, gamestate)
                
            elif action == "pa" and not any_fainted:
                gamestate = resetbattle(gamestate)
                gamestate = playgame(gamestate, element, newgame=False, skip_names=True)
                history = addtohistory(history, gamestate)
        else:
            print("\n\nThank you for playing!")
            if history['games_played'] > 0:
                displayhistory(history)
            break
    
    return

mainloop()
