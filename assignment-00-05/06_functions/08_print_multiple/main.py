def print_number(message, repeats):
    for _ in range(repeats):
        print(message, end=' ')

def main():
    message = input("Enter a message: ")
    repeats = int(input("Enter the number of times to repeat the message: "))
    print_number(message, repeats)

    
if __name__ == "__main__":
    main()
            
