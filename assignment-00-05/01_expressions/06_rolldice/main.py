import random

def main():

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    total = die1 + die2

    print(f"First die roll is {die1}")
    print(f"Second die roll is {die2}")
    print(f"Total roll is {total}")

if __name__ == "__main__":
    main()
        