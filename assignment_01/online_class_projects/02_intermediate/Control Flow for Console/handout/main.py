import random

NUM_ROUNDS = 3  # Define the number of rounds

def play_game():
    score = 0  # To keep track of the player's score

    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"\nRound {round_number}:")

        # Generate random numbers for each round
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        print(f"Your number: {user_number}")

        # Ask the user for their guess
        guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").lower()

        # Safeguard for valid input
        while guess not in ['higher', 'lower']:
            guess = input("Invalid input! Please enter either 'higher' or 'lower': ").lower()

        # Game logic to check if the guess is correct
        if guess == 'higher' and user_number > computer_number:
            print("You were right!")
            score += 1  # Increment score
        elif guess == 'lower' and user_number < computer_number:
            print("You were right!")
            score += 1  # Increment score
        else:
            print("You were wrong!")
        
        # Show the computer's number for transparency
        print(f"The computer's number was: {computer_number}")
        print(f"Your score is now: {score}")

    # End of game message
    print(f"\nGame Over! Your final score is {score}")

    # Conditional messages based on score
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Start the game
if __name__ == '__main__':
    play_game()
