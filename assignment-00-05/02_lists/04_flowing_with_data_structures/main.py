def add_three_copies(lst, data):

    lst.append(data)
    lst.append(data)
    lst.append(data)

message = input("Enter a message to copy : ")
my_list = []

print(f"List before: {my_list}")
add_three_copies(my_list, message)
print(f"List after: {my_list}")


