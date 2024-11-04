operands = ["a", "b", "c", "d", "e", "f", "g", "x"]

while True:
    # Ask for the operation
    operand = input("""
    What operation do you want to perform?
    a. Addition
    b. Subtraction
    c. Multiplication
    d. Division
    e. Modulus Division
    f. Exponent
    g. Floor Division
    x. Exit

    Enter the letter of the operation: """).lower()

    if operand == "x":
        print("\n\tExiting...Thank you!")
        exit()
    elif operand in operands:
        user_input = []

        for i in range(2):
            while True:
                user = input("\tEnter a non-negative integer or decimal number: ")
                if user.replace('.', '', 1).isdigit() and float(user) >= 0:
                    user_input.append(float(user))
                    break
                else:
                    print("\tInvalid input, please enter a valid non-negative number.")
        if user_input[0] < 0 or user_input[1] < 0:
            print("\tPlease input non-negative numbers")
        else:
            if operand == "a":
                print(f"\n\tThe sum of those numbers is {user_input[0] + user_input[1]}")
            elif operand == "b":
                print(f"\n\tThe difference of those numbers is {user_input[0] - user_input[1]}")
            elif operand == "c":
                print(f"\n\tThe product of those numbers is {user_input[0] * user_input[1]}")
            elif operand == "d":
                if user_input[0] == 0 or user_input[1] == 0:
                    print("\n\tDividing with zero is unavailable!")
                else:
                    print(f"\n\tThe quotient of those numbers is {user_input[0] / user_input[1]}")
            elif operand == "e":
                if user_input[0] == 0 or user_input[1] == 0:
                    print("\n\tDividing with zero is unavailable!")
                else:
                    print(f"\n\tThe modulus of those numbers is {user_input[0] % user_input[1]}")
            elif operand == "f":
                print(f"\n\tThe result of {user_input[0]} raised to the power of {user_input[1]} is {user_input[0] ** user_input[1]}")
            elif operand == "g":
                if user_input[0] == 0 or user_input[1] == 0:
                    print("\n\tDividing with zero is unavailable!")
                else:
                    print(f"\n\tThe floor division of those numbers is {user_input[0] // user_input[1]}")
    else:
        print("Invalid input for operand!")
