import random


DONE_LIKELIHOOD = 0.2


def done():
    return random.random() < DONE_LIKELIHOOD


def chaotic_counting():
    for number in range(1, 11):  
        if done():  
            return  
        print(number, end=" ")  


def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")


main()
