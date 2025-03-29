import random

def guess_my_number():
    # Step 1: Randomly select a number between 0 and 99
    number_to_guess = random.randint(1, 100)
    print("I am thinking of a number between 0 and 99...")

    # Step 2: Start the guessing process
    while True:
        try:
            # Step 3: Take input from the player
            guess = int(input("Enter a guess: "))
            
            # Step 4: Check if the guess is too high, too low, or correct
            if guess > number_to_guess:
                print("Your guess is too high")
            elif guess < number_to_guess:
                print("Your guess is too low")
            else:
                print(f"Congrats! The number was: {number_to_guess}")
                break  # Exit the loop when guessed correctly
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    guess_my_number()
