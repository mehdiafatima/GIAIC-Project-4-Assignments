def main():
    for number in range(10,19):
        if number % 2 == 0:
            print(f"{number} is even ", end="")
        else:
            print(f"{number} is odd ", end="")

if __name__ == "__main__":
    main()