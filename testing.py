import random as rm  # Import necessary modules: random for generating random numbers, and tabulate for formatting tables.
from tabulate import tabulate

# Dictionary to store Pokémon data. Each key represents a Pokémon and maps to a list containing:
# - Pokémon's name
# - Base power
# - Rank (used to influence battle outcomes)
pokemon_dict = {
    "a": ["Jigglypuff", 45, 1],
    "b": ["Pikachu", 50, 9],
    "c": ["Eevee", 52, 5],
    "d": ["Charmander", 55, 7],
    "e": ["Squirtle", 58, 6],
    "f": ["Bulbasaur", 60, 4],
    "g": ["Gengar", 70, 10],
    "h": ["Machamp", 75, 3],
    "i": ["Snorlax", 80, 8],
    "j": ["Mewtwo", 90, 2],
}

# Print a welcome message and instructions for the game.
print("""
Welcome to the Pokémon Battle Arena!

In this game, you'll choose your favorite Pokémon to battle against a randomly selected opponent. 
Each Pokémon has its own unique power and rank, and your goal is to defeat as many opponents as possible.

How to Play:

1. Choose your Pokémon from the list displayed.
2. Your Pokémon will battle against the computer's randomly selected Pokémon.
3. The power of each Pokémon will be determined by its base stats, 
with an added random variation to keep the battles exciting.
4. After each round, you'll see the result of the battle and have the option to play again or exit the game.

Objective: Outsmart the computer by choosing the right Pokémon and securing as many wins as possible! 
Track your victories and see who reigns supreme in the final battle summary.
""")

# Display the list of available Pokémon for the user to choose from.
counter = 0  # Initialize counter to format the display in rows of three.
for key, value_name in pokemon_dict.items():
    print(f"{key}. {value_name[0]:<11}", end="")  # Print Pokémon key and name.
    counter += 1
    if counter == 3:  # After every three Pokémon, start a new line.
        print()
        counter = 0

# Initialize variables to track the state of the game.
rounds_played, user_wins, computer_wins, ties = 0, 0, 0, 0  # Track number of rounds, wins, and ties.
round_details = []  # List to store details of each battle round.
user, computer_key = None, None  # Variables to hold the chosen Pokémon for user and computer.
final_user_power = 0  # Track user's power, carried over if they win.
final_computer_power = 0  # Track computer's power, carried over if they win.

# Main game loop. This runs continuously until the user decides to quit.
while True:
    # User selects a Pokémon.
    if user is None:  # If no Pokémon has been selected by the user yet.
        user = input("\nChoose your Pokemon: ").lower()  # Prompt the user to select one.
        if user not in pokemon_dict:  # Validate the selection.
            print("Invalid choice, try again.")  # Notify if the selection is invalid.
            user = None  # Reset the user's choice.
            continue  # Go back to the beginning of the loop to prompt again.

    # Computer randomly selects a Pokémon.
    if computer_key is None:  # If the computer hasn't selected a Pokémon yet.
        computer_key = rm.choice(list(pokemon_dict.keys()))  # Randomly choose a Pokémon for the computer.

    # Calculate the base power for both the user and computer, considering any power carried over from previous wins.
    base_user = pokemon_dict[user][1] + final_user_power  # User's base power + absorbed power from previous wins.
    base_computer = pokemon_dict[computer_key][1] + final_computer_power  # Computer's base power + absorbed power.

    # Determine the outcome based on the ranks and introduce random variations to keep the battles unpredictable.
    if pokemon_dict[user][2] < pokemon_dict[computer_key][2]:  # If user's Pokémon has a lower rank.
        random_variation = rm.randrange(0, 45, 5)  # Apply random variation to the power.
        final_user_power = base_user + random_variation  # Increase user's power by the random variation.
        final_computer_power = base_computer - random_variation  # Decrease computer's power by the random variation.
    else:  # If user's Pokémon has an equal or higher rank.
        random_variation = rm.randint(0, 45)  # Apply a different random variation.
        final_user_power = base_user - random_variation  # Decrease user's power by the random variation.
        final_computer_power = base_computer + random_variation  # Increase computer's power.

    # Display the battle results.
    print(f"User chose {pokemon_dict[user][0]} with power {final_user_power}")  # Show user's Pokémon and final power.
    print(f"Computer chose {pokemon_dict[computer_key][0]} with power {final_computer_power}")  # Show computer's Pokémon and final power.

    # Determine the winner of the battle.
    if final_user_power > final_computer_power:  # User wins the battle.
        print("User won!")  # Notify the user of their victory.
        user_wins += 1  # Increment user's win count.
        status = "User won"  # Set status for this round.
        user_pick = pokemon_dict[user][0]  # Record user's Pokémon.
        computer_pick = pokemon_dict[computer_key][0]  # Record computer's Pokémon.
        final_user_power += final_computer_power  # User absorbs the computer's power.
        computer_key = None  # Reset computer's Pokémon for the next round.
        rounds_played += 1  # Increment the number of rounds played.
        round_details.append([rounds_played, user_pick, final_user_power, computer_pick, final_computer_power, status])  # Log round details.

        # Prompt user to continue, choose a new Pokémon, or quit.
        while True:
            game = input("\n'C' to continue to battle\n'N' for new character selection\n'X' to quit\nWould you like to proceed? ").lower()
            if game == "c":  # Continue the battle.
                computer_key = rm.choice(list(pokemon_dict.keys())) if computer_key is None else computer_key  # Randomly select a new Pokémon for the computer if needed.
                break  # Exit the prompt loop.
            elif game == "n":  # Choose a new Pokémon.
                user = None  # Reset user's choice.
                break  # Exit the prompt loop.
            elif game == "x":  # Quit the game.
                # Display the final results with all rounds detailed.
                print("\nRound Details:")
                print(tabulate(round_details, headers=["Battle number", "User pokemon", "User power", "Computer pokemon", "Computer power", "Status"], tablefmt="grid"))
                if user_wins > computer_wins:  # Determine the overall winner.
                    print("\nOverall Result: User won more rounds!")
                elif computer_wins > user_wins:
                    print("\nOverall Result: Computer won more rounds!")
                else:
                    print("\nOverall Result: It's a tie overall!")
                exit()  # End the game.
            else:
                print("Invalid input, please try again.")  # Handle invalid input.

    elif final_user_power < final_computer_power:  # Computer wins the battle.
        print("Computer won!")  # Notify the user of their loss.
        computer_wins += 1  # Increment computer's win count.
        status = "Computer won"  # Set status for this round.
        user_pick = pokemon_dict[user][0]  # Record user's Pokémon.
        computer_pick = pokemon_dict[computer_key][0]  # Record computer's Pokémon.
        final_computer_power += final_user_power  # Computer absorbs user's power.
        user = None  # User must choose a new Pokémon.
        rounds_played += 1  # Increment the number of rounds played.
        round_details.append([rounds_played, user_pick, final_user_power, computer_pick, final_computer_power, status])  # Log round details.

        # Prompt user to choose a new Pokémon or quit.
        while True:
            game = input("\n'N' for new character selection\n'X' to quit\nWould you like to proceed? ").lower()
            if game == "c":  # Continue the battle.
                computer_key = rm.choice(list(pokemon_dict.keys())) if computer_key is None else computer_key  # Randomly select a new Pokémon for the computer if needed.
                break  # Exit the prompt loop.
            elif game == "n":  # Choose a new Pokémon.
                user = None  # Reset user's choice.
                break  # Exit the prompt loop.
            elif game == "x":  # Quit the game.
                # Display the final results with all rounds detailed.
                print("\nRound Details:")
                print(tabulate(round_details, headers=["Battle number", "User pokemon", "User power", "Computer pokemon", "Computer power", "Status"], tablefmt="grid"))
                if user_wins > computer_wins:  # Determine the overall winner.
                    print("\nOverall Result: User won more rounds!")
                elif computer_wins > user_wins:
                    print("\nOverall Result: Computer won more rounds!")
                else:
                    print("\nOverall Result: It's a tie overall!")
                exit()  # End the game.
            else:
                print("Invalid input, please try again.")  # Handle invalid input.

    else:  # If it's a tie.
        print("It's a tie!")  # Notify the user of the tie.
        ties += 1  # Increment tie count.
        status = "It's a tie"  # Set status for this round.
        user_pick = pokemon_dict[user][0]  # Record user's Pokémon.
        computer_pick = pokemon_dict[computer_key][0]  # Record computer's Pokémon.
        rounds_played += 1  # Increment the number of rounds played.
        round_details.append([rounds_played, user_pick, final_user_power, computer_pick, final_computer_power, status])  # Log round details.
