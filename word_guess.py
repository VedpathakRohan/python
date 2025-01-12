import random


def jumbled_word_game():
    print("Welcome to the Jumbled Word Game!")
    print("Unscramble the letters to guess the word.")
    print("Type 'quit' to exit the game.")

    words = ["python", "java", "random", "computer", "science", "programming", "data", "algorithm"]
    score = 0

    while True:
        # Select a random word and jumble its letters
        word = random.choice(words)
        jumbled = ''.join(random.sample(word, len(word)))

        print(f"Jumbled word: {jumbled}")

        # Get the player's guess
        user_guess = input("Your guess: ").lower()

        if user_guess == "quit":
            print(f"Thanks for playing! Your final score is: {score}")
            break
        elif user_guess == word:
            print("Correct! You guessed the word!")
            score += 1
        else:
            print(f"Wrong! The correct word was: {word}")


# Run the game
jumbled_word_game()
