def double_until_hundred():

    curr_value = int(input("Enter a starting value:"))

    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end="")


double_until_hundred()
