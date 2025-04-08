import random   
def guess(x):
 random_number = random.randint(1, x)
 guess = 0

 while guess != random_number:
     guess = int(input(f"guess a number between 1 and {x}: "))
     if guess < random_number:
        print("The number is lower than your guess.")
     elif guess > random_number:
        print("The number is higher than your guess.")

 print(f"Congratulations! You have guessed the number {random_number} correctly.")   

guess(10)
 


