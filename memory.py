import random
import time


def number_memory_game():
    print("Welcome to the Number Memory Game!")
    print("A number will be displayed for a few seconds. Memorize it!")
    print("Type the number correctly to score points.")
    print("Type 'quit' to exit the game.")

    score = 0
    level = 1

    while True:
        # Generate a random number with digits increasing based on level
        number_length = level + 2
        number_to_memorize = ''.join(random.choices('0123456789', k=number_length))

        print(f"Level {level}: Memorize this number")
        print(number_to_memorize)

        # Display the number for a few seconds, then clear it
        time.sleep(3)
        print("\n" * 50)  # Clear the screen by printing new lines

        # Prompt user to input the number
        user_guess = input("Enter the number: ").strip()

        if user_guess.lower() == "quit":
            print(f"Thanks for playing! Your final score is: {score}")
            break

        if user_guess == number_to_memorize:
            print("Correct! Moving to the next level.")
            score += 1
            level += 1
        else:
            print(f"Wrong! The correct number was: {number_to_memorize}")
            print(f"Your final score is: {score}")
            break


# Run the game
number_memory_game()
