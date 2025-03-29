def main():
    # Fruit prices dictionary
    fruit_prices = {
        "apple": 3.0,
        "durian": 5.0,
        "jackfruit": 7.5,
        "kiwi": 4.0,
        "rambutan": 2.5,
        "mango": 6.0
    }

    total_cost = 0  # Initialize total cost

    for fruit in fruit_prices:
        while True:  # Loop until valid input is received
            try:
                quantity = input(f"How many ({fruit}) do you want?: ")
                if quantity == "":  # Handle empty input
                    quantity = 0
                else:
                    quantity = int(quantity)  # Convert input to integer
                break  # Exit loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a number.")

        total_cost += quantity * fruit_prices[fruit]  # Calculate cost for each fruit

    print(f"\nYour total is ${total_cost:.2f}")  # Display total cost


if __name__ == '__main__':
    main()
