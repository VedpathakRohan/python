import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)

    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            # Get user's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Run the game
number_guessing_game()
