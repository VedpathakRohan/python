import random


def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

    choices = ["rock", "paper", "scissors"]
    wins, losses, ties = 0, 0, 0

    while True:
        user_choice = input("Your choice: ").lower()
        if user_choice == "quit":
            print("Thanks for playing!")
            print(f"Final Score: {wins} Wins, {losses} Losses, {ties} Ties.")
            break
        if user_choice not in choices:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1


# Run the game
rock_paper_scissors()
