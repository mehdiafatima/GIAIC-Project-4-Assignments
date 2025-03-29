# Define the minimum height required to ride
MINIMUM_HEIGHT = 24

def tall_enough():
    """
    Check if the user is tall enough to ride based on their input height.
    """
    # Loop to continuously ask the user for their height
    while True:
        height_input = input("How tall are you? (Press Enter to stop): ")

        # Check if the user pressed Enter without typing anything
        if height_input.strip() == "":
            print("Program stopped. Thank you!")
            break

        # Convert the input into an integer
        try:
            height = int(height_input)
        except ValueError:
            print("Please enter a valid number for your height.")
            continue

        # Check if the user meets the minimum height requirement
        if height >= MINIMUM_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# Required boilerplate to run the function
if __name__ == "__main__":
    tall_enough()
