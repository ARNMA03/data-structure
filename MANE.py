



'''import random

# Information about the game
def info():
    print("Hello Trainers, Welcome to the Battle of the Pokémons!")
    print("First, you need to choose your own Pokémon. After you choose, the battle begins.")
    print("If you win the battle against the computer opponent, your Pokémon's power will increase.")
    print("You can continue to the next battle using the same Pokémon and you can also change your Pokémon if you want.")
    print("\nEnjoy the battle!\n")
    print("Press 'x' to quit the battle.")

# List of Pokémons and their base power
pokemons = {
    'Pikachu': 50,
    'Charmander': 55,
    'Bulbasaur': 60,
    'Squirtle': 58,
    'Jigglypuff': 45,
    'Eevee': 52,
    'Snorlax': 80,
    'Gengar': 70,
    'Machamp': 75,
    'Mewtwo': 90}

# Trainer Choosing of Pokémon
def choose_pokemon():
    print("\nChoose your own Pokémon:")
    for name in pokemons:
        print(f"{name} (Base Power: {pokemons[name]})")
    chosen = input("\nType the name of your Pokémon: ").capitalize()
    if chosen in pokemons:
        return chosen, pokemons[chosen]
    else:
        print("Invalid input. Please select another Pokémon from the list.")
        return choose_pokemon()

# Adding the base power of the opponent kineme
def add_power(base_power):
    hello = random.randint(-10, 10)
    return abs(base_power * hello)

# Computer Opponent Choosing a Pokémon
def opponent():
    oops, oops_power = random.choice(list(pokemons.items()))
    werpa = add_power(oops_power)
    print(f"Selected Pokémon of the Computer: {oops} (Final Power: {werpa})")
    return oops, werpa

# Battle of base power trainers vs computer opponent
def battle(us_power, com_power):
    if us_power > com_power:
        return "Win"
    elif us_power < com_power:
        return "Lose"
    else:
        return "Tie"

# Tally who wins
def tally_who_win(us_win, com_win):
    if us_win > com_win:
        print(f"\nTrainer won {us_win} game/games. The computer won {com_win} game/games.")
        print("Congratulations! You are the overall champion!")
    elif com_win > us_win:
        print(f"Trainer won {us_win} game/games. The computer won {com_win} game/games.")
        print("Computer is the overall winner!")
    else:
        print(f"Congratulations! It's a tie! Number of wins: {us_win} game/games")

# Function to display the battle summary in a table format
def display_battle_summary(battles):
    print("\nBattle Summary:")
    print(f"\n{'Battle Number':<15}{'User Power':<15}{'Computer Power':<20}{'Status':<10}")
    print("-" * 60)
    for battle in battles:
        print(f"{battle['battle_number']:<15}{battle['user_power']:<15}{battle['computer_power']:<20}{battle['status']:<10}")

# Working of the game
def cute():
    info()
    us_con = True
    bat_number = 0
    total = 0
    us_win = 0
    com_win = 0
    battles = []  # List to store the results of each battle

    while us_con:
        if total == 0 or input("\nContinue with the same Pokémon? (c to continue, n to choose new): ").lower() == 'n':
            pona, bapo = choose_pokemon()
            uspo = add_power(bapo)
            print(f"\nSelected Pokémon of the Trainer: {pona} (Final Power: {uspo})")
        else:
            uspo = total

        com_name, com_power = opponent()

        result = battle(uspo, com_power)
        bat_number += 1

        # Store battle details in the list
        battles.append({
            'battle_number': bat_number,
            'user_power': uspo,
            'computer_power': com_power,
            'status': "Trainer Wins!" if result == "Win" else "Computer Wins!" if result == "Lose" else "Tie"
        })

        if result == "Win":
            us_win += 1
            total = uspo + com_power
            print(f"\nRound: {bat_number}")
            print(f"Trainer's Pokémon Power: {uspo}")
            print(f"Computer's Pokémon Power: {com_power}")
            print("Status: Trainer Wins!")
            print("\nNice Choice!")

        elif result == "Lose":
            com_win += 1
            total = uspo + com_power
            print(f"\nRound: {bat_number}")
            print(f"Trainer's Pokémon Power: {uspo}")
            print(f"Computer's Pokémon Power: {com_power}")
            print("Status: Computer Wins!")
            print("\nGame Over! 🙁 ")
            total = 0

        else:
            print(f"\nRound: {bat_number}")
            print(f"Trainer's Pokémon Power: {uspo}")
            print(f"Computer's Pokémon Power: {com_power}")
            print("Status: Tie!\n")

        user_input = input("\nDo you wish to continue playing? (Press 'x' to exit, Press any other key to continue): ").lower()
        if user_input == 'x':
            tally_who_win(us_win, com_win)
            display_battle_summary(battles)  # Display the battle summary at the end of the game
            print("\nExcellent Battle! Thank you for playing!")
            print("I hope you enjoy the battle!\n")
            us_con = False

cute()'''