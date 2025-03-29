def main():
    phonebook = {}  # Dictionary to store contacts

    while True:
        print("\n1. Add Contact  2. View Contacts  3. Search  4. Delete  5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:  # Add contact
            name = input("Enter name: ")
            number = input("Enter number: ")
            phonebook[name] = number  
            print(f"Added: {name} - {number}")

        elif choice == 2:  # View all contacts
            if phonebook:
                for name, number in phonebook.items():
                    print(f"{name}: {number}")
            else:
                print("No contacts to show!")

        elif choice == 3:  # Search for a contact
            name = input("Enter name to search: ")
            print(f"{name}: {phonebook.get(name, 'Not found')}")

        elif choice == 4:  # Delete a contact
            name = input("Enter name to delete: ")
            if name in phonebook:
                del phonebook[name]
                print(f"Deleted: {name}")
            else:
                print("Contact not found!")

        elif choice == 5:  # Exit the program
            print("Goodbye!")
            break

        else:  # Handle invalid input
            print("Invalid choice! Try again.")

if __name__ == '__main__':
    main()
