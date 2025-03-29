MAX_VALUE = 1000

def fibonacci_sequence(max_value):
    fib1, fib2 = 0, 1
    print(fib1, end="")

    while fib2 < max_value:
        print(fib2, end="")
        fib1, fib2 = fib2, fib1 + fib2

fibonacci_sequence(MAX_VALUE)