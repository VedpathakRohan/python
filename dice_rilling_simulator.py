import random

def dice_rolling_simulator():
    print("Welcome to the Dice Rolling Simulator!")
    print("Press 'r' to roll the dice or 'q' to quit.")

    while True:
        user_input = input("Your choice (r/q): ").lower()
        if user_input == 'r':
            dice_roll = random.randint(1, 6)
            print(f"The dice rolled: {dice_roll}")
        elif user_input == 'q':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input! Please press 'r' to roll or 'q' to quit.")

# Run the gamer
dice_rolling_simulator()
