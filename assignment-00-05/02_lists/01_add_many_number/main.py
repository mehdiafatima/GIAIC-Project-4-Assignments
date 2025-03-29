def sum_of_numbers(numbers):
   
    total = sum(numbers)  # Use the built-in sum() function to calculate the total
    return total


numbers_list = [1, 8, 40, 2, 5]  # Example list of numbers
result = sum_of_numbers(numbers_list)
print(f"The sum of the numbers {numbers_list} is: {result}")
