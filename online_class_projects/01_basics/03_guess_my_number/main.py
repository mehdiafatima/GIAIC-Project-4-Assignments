import random  

def main():
    
    number_to_guess = random.randint(0, 99)
    
    while True:
       
        user_guess = int(input("Enter a guess: "))
        
        
        if user_guess < number_to_guess:
            print("Your guess is too low")
        elif user_guess > number_to_guess:
            print("Your guess is too high")
        else:
        
            print(f"Congrats! The number was: {number_to_guess}")
            break  


if __name__ == '__main__':
    main()
