def main():
    fruit = input("Enter a fruit name : ")
    stock = num_in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock. Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock")

def num_in_stock(fruit):
    inventory = {
        "apple": 10,
        "banana": 0,
        "orange": 5,
        "grape": 2,
        "peach": 0,
        "pineapple": 29,
        "kiwi": 6,
        "strawberry": 7,
        "watermelon": 9,
    }    
    return inventory.get(fruit, 0)


if __name__ == "__main__":
    main()
    
