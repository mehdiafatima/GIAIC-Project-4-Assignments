import random 

print("Welcome To Your Password Generator 🔏")

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+{}:"<>?[];\'\\,./`~'

number = int(input("How many passwords do you want to generate? : "))
length = int(input("How long do you want your passwords to be? : "))

print("\nHere are your passwords: \n")

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
print("\nThanks for using the Password Generator!🌺")    

