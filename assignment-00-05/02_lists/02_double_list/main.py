def double_numbers(numbers):
    doubled = [num * 2 for num in numbers]  # Multiply each number in the list by 2
    return doubled


numbers = [9, 2, 6, 4]  # Original list
doubled_numbers = double_numbers(numbers)  # Double each number
print(f"Original list: {numbers}")
print(f"Doubled list: {doubled_numbers}")
