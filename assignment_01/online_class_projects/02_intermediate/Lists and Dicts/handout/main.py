def main():
    fruit_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print(len(fruit_list))

    fruit_list.append('mango')
    print("Updated list:", fruit_list)  


def access_element(my_list, index):
    if index >= len(my_list) or index < 0:
        return "Index out of range!"
    else:
        return my_list[index] 


def modify_element(my_list, index, new_value):
    if index >= len(my_list) or index < 0:
        return "Index out of range!" 
    else:
        my_list[index] = new_value 
        return my_list


def slice_list(my_list, start_index, end_index):
    if start_index < 0 or end_index > len(my_list) or start_index >= end_index:
        return "Invalid slice indices!"
    else:
        return my_list[start_index:end_index]


def main():
    my_list = [3, 'apple', 7, 'banana', 5]

    print("Select an operation: ")
    print("1. Access an element")
    print("2. Modify an element")
    print("3. Slice the list")

    operation = int(input("Enter operation number: "))  

    if operation == 1:
        index = int(input("Enter index to access: ")) 
        print(access_element(my_list, index))

    elif operation == 2:
        index = int(input("Enter index to modify: ")) 
        new_value = input("Enter new value: ")  
        print(modify_element(my_list, index, new_value)) 

    elif operation == 3:
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: ")) 
        print(slice_list(my_list, start, end)) 
    
    else:
        print("Invalid operation!")  


if __name__ == "__main__":
    main()
