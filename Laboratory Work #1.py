import random as rm
from tabulate import tabulate

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

# Display Pokemon List
counter = 0
for key, value_name in pokemon_dict.items():
   print(f"{key}. {value_name[0]:<11}, Base power: {value_name[1]:<10}", end="")
   counter += 1
   if counter == 5:
       print()
       counter = 0

# Initialize Game Variables
rounds_played, user_wins, computer_wins, ties = 0, 0, 0, 0
round_details = []
user, computer_key = None, None
final_user_power = 0  # Initialize winner's power
final_computer_power = 0  # Initialize loser's power

# Main Game Loop
while True:
   #  User Pokemon Selection
   if user is None:
       user = input("\nChoose your Pokemon: ").lower()
       if user not in pokemon_dict:
           print("Invalid choice, try again.")
           user = None
           continue  # Prompt user again

   # Computer Pokemon Selection
   if computer_key is None:
       computer_key = rm.choice(list(pokemon_dict.keys()))

   base_user = pokemon_dict[user][1] + final_user_power  # Use retained winner's power
   base_computer = pokemon_dict[computer_key][1] + final_computer_power  # Use retained loser's power

   # Power Calculation

   if pokemon_dict[user][2] < pokemon_dict[computer_key][2]:
       random_variation = rm.uniform(0.01, 1.5)
       final_user_power = abs(base_computer + (base_user * random_variation))
       final_computer_power = abs(base_user - (base_computer * random_variation))
   else:
       random_variation = rm.uniform(0.01, 1.5)
       final_user_power = abs(base_computer - (base_user * random_variation))
       final_computer_power = abs(base_user + (base_computer * random_variation))

   # Display Battle Results
   print(f"User chose {pokemon_dict[user][0]} with power {final_user_power}")
   print(f"Computer chose {pokemon_dict[computer_key][0]} with power {final_computer_power}")

   # Determine Winner and Absorb Power
   if final_user_power > final_computer_power:
       print("User won!")
       user_wins += 1
       status = "User won"
       user_pick = pokemon_dict[user][0]
       computer_pick = pokemon_dict[computer_key][0]
       # Absorb computer's power
       final_user_power += final_computer_power  # Winner absorbs loser's power
       computer_key = None  # Reset computer's Pokémon for the next round
       rounds_played += 1
       round_details.append([rounds_played, user_pick, final_user_power, computer_pick, final_computer_power, status])
       while True:
           game = input(
               "\n'C' to continue to battle\n'N' for new character selection\n'X' to quit\nWould you like to proceed? ").lower()
           if game == "c":
               computer_key = None
               break
           elif game == "n":
               user = None  # Reset user choice
               final_user_power = 0  # Reset user power
               final_computer_power = 0  # Reset computer power
               break
           elif game == "x":
               # Display Final Results
               print("\nRound Details:")
               print(tabulate(round_details,
                              headers=["Battle number", "User pokemon", "User power", "Computer pokemon",
                                       "Computer power", "Status"],
                              tablefmt="grid"))
               if user_wins > computer_wins:
                   print("\nOverall Result: User won more rounds!")
               elif computer_wins > user_wins:
                   print("\nOverall Result: Computer won more rounds!")
               else:
                   print("\nOverall Result: It's a tie overall!")
               print(f"""                User won {user_wins} times
               Computer won {computer_wins} times
               Match tied {ties} times""")
               exit()
           else:
               print("Invalid input, please try again.")
   elif final_user_power < final_computer_power:
       print("Computer won!")
       computer_wins += 1
       status = "Computer won"
       user_pick = pokemon_dict[user][0]
       computer_pick = pokemon_dict[computer_key][0]
       # Absorb user's power
       final_computer_power += final_user_power  # Winner absorbs loser's power
       user = None  # User must select a new Pokémon
       rounds_played += 1
       round_details.append([rounds_played, user_pick, final_user_power, computer_pick, final_computer_power, status])
       while True:
           game = input(
               "\n'N' for new character selection\n'X' to quit\nWould you like to proceed? ").lower()
           if game == "n":
               user = None  # Reset user choice
               final_user_power = 0
               break
           elif game == "x":
               # Display Final Results
               print("\nRound Details:")
               print(tabulate(round_details,
                              headers=["Battle number", "User pokemon", "User power", "Computer pokemon",
                                       "Computer power", "Status"],
                              tablefmt="grid"))
               if user_wins > computer_wins:
                   print("\nOverall Result: User won more rounds!")
               elif computer_wins > user_wins:
                   print("\nOverall Result: Computer won more rounds!")
               else:
                   print("\nOverall Result: It's a tie overall!")
               print(f"""                User won {user_wins} times
               Computer won {computer_wins} times
               Match tied {ties} times""")
               exit()
           else:
               print("Invalid input, please try again.")

   else:
       print("It's a tie!")
       ties += 1
       status = "Tie"
       user_pick = pokemon_dict[user][0]
       computer_pick = pokemon_dict[computer_key][0]
       user = None  # User must select a new Pokémon
       rounds_played += 1
       round_details.append([rounds_played, user_pick, final_user_power, computer_pick, final_computer_power, status])
       game = input(
           "\n'C' to continue to battle\n'N' for new character selection\n'X' to quit\nWould you like to proceed? ").lower()
       if game == "c":
           computer_key = None
           user = None
           break
       elif game == "n":
           user = None  # Reset user choice
           computer_key = None  # Reset computer choice
           final_user_power = 0  # Reset user power
           final_computer_power = 0  # Reset computer power
           break
       elif game == "x":
           # Display Final Results
           print("\nRound Details:")
           print(tabulate(round_details,
                          headers=["Battle number", "User pokemon", "User power", "Computer pokemon",
                                   "Computer power", "Status"],
                          tablefmt="grid"))
           if user_wins > computer_wins:
               print("\nOverall Result: User won more rounds!")
           elif computer_wins > user_wins:
               print("\nOverall Result: Computer won more rounds!")
           else:
               print("\nOverall Result: It's a tie overall!")
           print(f"""                User won {user_wins} times
           Computer won {computer_wins} times
           Match tied {ties} times""")
           exit()
       else:
           print("Invalid input, please try again.")


