import random
import time
from tabulate import tabulate

pokemon_lists = {
    "Pikachu": 50,
    "Charmander": 55,
    "Bulbasaur": 60,
    "Squirtle": 58,
    "Jigglypuff": 45,
    "Eevee": 52,
    "Snorlax": 80,
    "Gengar": 70,
    "Machamp": 75,
    "Mewtwo": 90
}

print("Welcome to the Masculino's Pokemon Battle Simulation!")
print("\nHere's how to play:")
print("   1. Select a Pokemon from the list.")
print("   2. Engage in a battle with a computer-generated Pokemon.")
print(
    "   3. After each battle, you can choose to \n     [c] continue with the same Pokemon, \n     [n] select a new one ('n'), or \n     [x] exit the game.")


def select_pokemon():
    while True:
        print("\nSelect your Pokemon:")
        for pokemon in pokemon_lists:
            print(f"- {pokemon}")
        user_pokemon = input("Enter the name of your Pokemon: ").strip().capitalize()
        if user_pokemon in pokemon_lists:
            return user_pokemon
        else:
            print("Invalid selection. Please try again.")


def get_pokemon_power(pokemon):
    return pokemon_lists[pokemon] + random.randint(-10, 10)


battle_results = []
user_wins = 0
computer_wins = 0

user_pokemon = select_pokemon()
user_power = get_pokemon_power(user_pokemon)

while True:
    computer_pokemon = random.choice(list(pokemon_lists.keys()))
    computer_power = get_pokemon_power(computer_pokemon)

    initial_user_power = user_power
    initial_computer_power = computer_power

    print(f"\nYour Pokemon: {user_pokemon} (Power: {user_power})")
    print(f"Computer's Pokemon: {computer_pokemon} (Power: {computer_power})")
    print("Battle begins...")

    time.sleep(2)  # Simulate a time interval before the battle result

    if user_power > computer_power:
        user_power += computer_power  # User wins, add opponent's power to user's power
        computer_power = 0  # Computer loses, set power to 0
        status = "User wins"
        user_wins += 1
        print("You win!")
    elif user_power < computer_power:
        computer_power += user_power  # Computer wins, add opponent's power to computer's power
        user_power = 0  # User loses, set power to 0
        status = "Computer wins"
        computer_wins += 1
        print("You lose!")
    else:
        status = "Tie"
        print("It's a tie!")

    battle_results.append([
        len(battle_results) + 1,
        user_pokemon,
        initial_user_power,
        computer_pokemon,
        initial_computer_power,
        status
    ])

    print("\nBattle Results:")
    print(f"Your {user_pokemon}'s updated power is {user_power}")
    print(f"Computer's {computer_pokemon} updated power is {computer_power}\n")

    if user_power == 0:
        print("Your Pokémon has no base power left. You can select a new one or exit the game.\n")
        choice = input(
            "Do you want to: \n   [n] select a new Pokemon, or \n   [x] exit the game? \nAnswer: ").strip().lower()
        if choice == 'n':
            user_pokemon = select_pokemon()
            user_power = get_pokemon_power(user_pokemon)
        elif choice == 'x':
            print("Thanks for playing!")
            print("\nSummary of Battles:")
            print(tabulate(battle_results,
                           headers=["Battle No.", "User Pokemon", "User Power", "Computer Pokemon", "Computer Power",
                                    "Status"], tablefmt="grid"))
            break
        else:
            print("Invalid input. Exiting the game.")
            print("\nSummary of Battles:")
            print(tabulate(battle_results,
                           headers=["Battle No.", "User Pokemon", "User Power", "Computer Pokemon", "Computer Power",
                                    "Status"], tablefmt="grid"))
            break
    else:
        choice = input(
            "Do you want to: \n   [c] continue with the same Pokemon, \n   [n] select a new one, or \n   [x] exit the game? \nAnswer: ").strip().lower()
        if choice == 'c':
            continue  # Ensure computer changes in the next battle
        elif choice == 'n':
            user_pokemon = select_pokemon()
            user_power = get_pokemon_power(user_pokemon)
        elif choice == 'x':
            print("Thanks for playing!")
            print("\nSummary of Battles:")
            print(tabulate(battle_results,
                           headers=["Battle No.", "User Pokemon", "User Power", "Computer Pokemon", "Computer Power",
                                    "Status"], tablefmt="grid"))
            break
        else:
            print("Invalid input. Exiting the game.")
            print("\nSummary of Battles:")
            print(tabulate(battle_results,
                           headers=["Battle No.", "User Pokemon", "User Power", "Computer Pokemon", "Computer Power",
                                    "Status"], tablefmt="grid"))
            break

# Overall Result Calculation
if user_wins > computer_wins:
    print("\nOverall Result: User won more rounds!")
elif computer_wins > user_wins:
    print("\nOverall Result: Computer won more rounds!")
else:
    print("\nOverall Result: It's a tie overall!")
