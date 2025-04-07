def double(num):
    return num * 2
    

def main():
    user_input = int(input("Enter a number: "))
    result = double(user_input)
    print(f"The double of {user_input} is {result}.")


if __name__ == "__main__":
    main()


