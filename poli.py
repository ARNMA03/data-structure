import random
import numpy as np
from tabulate import tabulate

#Initial Pokémon list
pokemon_names = np.array(["Pikachu", "Charmander", "Bulbasaur", "Squirtle", "Jigglypuff", "Snorlax", "Gengar", "Eevee"])
initial_health = 100.0  # All Pokémon start with 100 health
pokemon_health = np.full(len(pokemon_names), initial_health)
pokemon_power = np.array([50, 55, 45, 40, 30, 60, 70, 65], dtype=float)

#Potions available
healing_potions_available = 4  # Each player has 4 healing potions per round
poison_potions_available = 4  # Each player has 4 poison potions per round

#Player Pokémon Selection
def select_pokemon(player_name, available_pokemon, picks):
    print(f"\n{player_name}, please select {picks} Pokémon from the following list:")
    for idx, name in enumerate(available_pokemon):
        print(f"{idx + 1}: {name} (Health: {initial_health}, Power: {pokemon_power[np.where(pokemon_names == name)[0][0]]})")

    selected_pokemon = []
    for _ in range(picks):
        while True:
            try:
                choice = int(input(f"Select Pokémon by number (1-{len(available_pokemon)}): ")) - 1
                if 0 <= choice < len(available_pokemon):
                    selected_pokemon.append(available_pokemon[choice])
                    # Remove chosen Pokémon from available list
                    available_pokemon = np.delete(available_pokemon, choice)
                    break
                else:
                    print("Invalid choice. Please select again.")
            except ValueError:
                print("Please enter a valid number.")

    return np.array(selected_pokemon), available_pokemon

#Simulate Battle
def battle(pokemon1, pokemon2):
    index1 = np.where(pokemon_names == pokemon1)[0][0]
    index2 = np.where(pokemon_names == pokemon2)[0][0]

    print(f"\nBattle: {pokemon1} vs {pokemon2} | Power: {pokemon_power[index1]} vs {pokemon_power[index2]}")

    # Determine winner and adjust health
    if pokemon_power[index1] > pokemon_power[index2]:
        winner = pokemon1
        loser = pokemon2
        pokemon_health[index1] *= 1.05  # Winner health increases by 5%
        pokemon_health[index2] *= 0.90  # Loser health decreases by 10%
    elif pokemon_power[index2] > pokemon_power[index1]:
        winner = pokemon2
        loser = pokemon1
        pokemon_health[index2] *= 1.05  # Winner health increases by 5%
        pokemon_health[index1] *= 0.90  # Loser health decreases by 10%
    else:
        print("It's a tie!")
        return None, None

    # Fatigue: Decrease health by 2% for both Pokémon
    pokemon_health[index1] *= 0.98
    pokemon_health[index2] *= 0.98

    print(f"Winner: {winner} | Loser: {loser}")
    print(f"Updated Health: {pokemon1} = {pokemon_health[index1]:.2f}, {pokemon2} = {pokemon_health[index2]:.2f}")
    return winner, loser

#Use a healing potion to heal a Pokémon and increase its power
def use_healing_potion(pokemon):
    index = np.where(pokemon_names == pokemon)[0][0]
    if pokemon_health[index] > 0:  # Only heal if the Pokémon is still alive
        pokemon_health[index] += 20.0  # Heal by 20 points
        pokemon_power[index] += 5.0  # Increase power by 5
        print(f"{pokemon} used a healing potion! Health increased to {pokemon_health[index]:.2f}, Power increased to {pokemon_power[index]:.2f}.")

#Use a poison potion on an opponent's Pokémon and decrease their power
def use_poison_potion(pokemon):
    index = np.where(pokemon_names == pokemon)[0][0]
    if pokemon_health[index] > 0:  # Only poison if the Pokémon is still alive
        new_health = pokemon_health[index] - 15.0  # Calculate new health after poisoning
        if new_health < 0:
            new_health = 0  # Prevent health from going below zero
        pokemon_health[index] = new_health  # Update health
        pokemon_power[index] -= 5.0  # Decrease power by 5
        print(f"{pokemon} was poisoned! Health reduced to {pokemon_health[index]:.2f}, Power decreased to {pokemon_power[index]:.2f}.")

#Pair Pokémon for Battle
def pair_pokemon_for_battles(player1_pokemon, player2_pokemon):
    # Pair all Pokémon selected for battles
    num_battles = min(len(player1_pokemon), len(player2_pokemon))
    return list(zip(player1_pokemon[:num_battles], player2_pokemon[:num_battles]))

#Run Three Rounds
def play_game():
    total_battles = []
    overall_player1_wins = 0
    overall_player2_wins = 0

    #Input player names
    while True:
        player1_name = input("Enter the name of Player 1: ").strip()
        if player1_name:
            break
        print("Player 1 name cannot be blank. Please enter a valid name.")

    while True:
        player2_name = input("Enter the name of Player 2: ").strip()
        if player2_name:
            break
        print("Player 2 name cannot be blank. Please enter a valid name.")

    #Joint decision on number of Pokemon to select
    while True:
        try:
            picks = int(input("How many Pokémon do both players want to select (3 or 4)? "))
            if picks in [3, 4]:
                break
            else:
                print("Invalid input. Please select either 3 or 4 Pokémon.")
        except ValueError:
            print("Please enter a valid number.")

    available_pokemon = pokemon_names.copy()  # Reset available Pokémon for each round

    for round_number in range(3):  # Always play three rounds
        player1_wins = 0
        player2_wins = 0
        round_battles = []

        print(f"\n--- Round {round_number + 1} ---")

        # Reset potions for each round
        player1_healing_potions = healing_potions_available
        player1_poison_potions = poison_potions_available
        player2_healing_potions = healing_potions_available
        player2_poison_potions = poison_potions_available

        print(f"{player1_name} has {player1_healing_potions} healing potions and {player1_poison_potions} poison potions.")
        print(f"{player2_name} has {player2_healing_potions} healing potions and {player2_poison_potions} poison potions.")

        #Ask players if they want to reuse the same Pokémon or select new ones
        if round_number > 0:  
            while True:
                reuse_choice = input("Do you want to use the same Pokémon as the previous round? (yes/no): ").strip().lower()
                if reuse_choice == "yes":
                    print("Using previous Pokémon selections.")
                    break
                elif reuse_choice == "no":
                    #Reset health and power 
                    global pokemon_health
                    pokemon_health = np.full(len(pokemon_names), initial_health)  # Reset health
                    available_pokemon = pokemon_names.copy()  # Reset available Pokémon for new selections
                    player1_pokemon, available_pokemon = select_pokemon(player1_name, available_pokemon, picks)
                    player2_pokemon, available_pokemon = select_pokemon(player2_name, available_pokemon, picks)
                    break
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")

        #Both players select Pokémon 
        if round_number == 0:
            player1_pokemon, available_pokemon = select_pokemon(player1_name, available_pokemon, picks)
            player2_pokemon, available_pokemon = select_pokemon(player2_name, available_pokemon, picks)

        #Pair Pokémon for battles based on the number selected (3 or 4)
        for p1, p2 in pair_pokemon_for_battles(player1_pokemon, player2_pokemon):
            #Player 1
            while True:
                use_healing_choice = input(f"{player1_name}: Do you want to use a healing potion on {p1}? (yes/no): ").strip().lower()
                if use_healing_choice == "yes" and player1_healing_potions > 0:
                    use_healing_potion(p1)
                    player1_healing_potions -= 1
                    break
                elif use_healing_choice == "no":
                    break
                else:
                    print("Invalid choice or no healing potions left.")

            #Player 2
            while True:
                use_healing_choice = input(f"{player2_name}: Do you want to use a healing potion on {p2}? (yes/no): ").strip().lower()
                if use_healing_choice == "yes" and player2_healing_potions > 0:
                    use_healing_potion(p2)
                    player2_healing_potions -= 1
                    break
                elif use_healing_choice == "no":
                    break
                else:
                    print("Invalid choice or no healing potions left.")

            #Players can choose to use poison potions
            while True:
                use_poison_choice = input(f"{player1_name}: Do you want to use a poison potion on {p2}? (yes/no): ").strip().lower()
                if use_poison_choice == "yes" and player1_poison_potions > 0:
                    use_poison_potion(p2)
                    player1_poison_potions -= 1
                    break
                elif use_poison_choice == "no":
                    break
                else:
                    print("Invalid choice or no poison potions left.")

            while True:
                use_poison_choice = input(f"{player2_name}: Do you want to use a poison potion on {p1}? (yes/no): ").strip().lower()
                if use_poison_choice == "yes" and player2_poison_potions > 0:
                    use_poison_potion(p1)
                    player2_poison_potions -= 1
                    break
                elif use_poison_choice == "no":
                    break
                else:
                    print("Invalid choice or no poison potions left.")

            #battle outcome
            winner, loser = battle(p1, p2)
            if winner:
                round_battles.append([p1, p2, winner, loser])  # Store battle results with actual winner and loser
                if winner == p1:
                    player1_wins += 1
                else:
                    player2_wins += 1
            else:
                round_battles.append([p1, p2, "Tie", "N/A"])  # Store as a tie

        total_battles.append(round_battles)
        overall_player1_wins += player1_wins
        overall_player2_wins += player2_wins

        print(f"\n{player1_name} won {player1_wins} battles this round.")
        print(f"{player2_name} won {player2_wins} battles this round.")

        #Print overall wins 
        print(f"Overall Wins after Round {round_number + 1}:")
        print(f"{player1_name}: {overall_player1_wins} wins")
        print(f"{player2_name}: {overall_player2_wins} wins")

    #Final results
    print(f"\n--- Final Results ---")
    print(f"{player1_name} won a total of {overall_player1_wins} battles.")
    print(f"{player2_name} won a total of {overall_player2_wins} battles.")

# Start the game
play_game()

