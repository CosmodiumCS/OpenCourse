# for this module's practice:
# we will make the game "Rock, Paper, Scissors" [rps]

# created by : C0SM0

# import random module, "r"
import random as r 

# loop code, avoid exception
while True:
    # banner
    print("Rock, Paper, Scissors")

    # available options
    options = ("Rock", "Paper", "Scissors")

    # option menu
    print("Choose your move:\n1) Rock\n2) Paper\n3) Scissors\n")

    # try to get integer user input
    try:
        # user input, option
        user_option = int(input("Option : "))
        comp_option = r.choice(options)
        
        # rock
        if user_option == 1:
            user_move = options[0]

        # paper
        elif user_option == 2:
            user_move = options[1]

        # scissors
        elif user_option == 3:
            user_move = options[2]

        # exception
        else:
            print("Invalid option, try again\n")
            continue

        # shoot
        print("\nRock...\nPaper...\nScissors...\nSHOOT!\n")
        print(f"Your move : {user_move}")
        print(f"Computer move : {comp_option}")

        # calculates draw
        if user_move == comp_option:
            print("Draw :|\n\n")
            break

        # calculates loss
        elif (user_move == options[0] and comp_option == options[1]) or (user_move == options[1] and comp_option == options[2]) or (user_move == options[2] and comp_option == options[1]):
            print("You lose :(\n\n")
            break

        # calcualtes win
        else:
            print("You Win :)")
            break

    # exception
    except ValueError:
        print("Enter a whole number option [1, 2, or 3]\n")

# feel free to keep practicing, here are some more ideas
"""
- a money/coin counter
- a minimal calculator
"""