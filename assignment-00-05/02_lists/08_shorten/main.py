MAX_LENGTH = 4 

def shorten(lst):

    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()
        print(f"Removed element: {removed_element}")

def main():
 
    user_input = input("Enter a list of items separated by spaces: ")
    lst = user_input.split()  

    print(f"Original list: {lst}")  
    shorten(lst) 
    print(f"Final list: {lst}") 


if __name__ == '__main__':
    main()        
