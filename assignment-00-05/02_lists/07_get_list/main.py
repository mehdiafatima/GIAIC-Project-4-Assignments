def main():
    values_list = []

    while True:
        user_input = input("Enter a value: ")

        if user_input == "":
            break

        values_list.append(user_input)

    print(f"Here's the list:", values_list)    

if __name__ == "__main__":
    main()