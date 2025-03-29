def main():
    counts= {}

    while True:
        number = input("Enter a number (or press ENTER to stop) : ")

        if number =="":
            break 

        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1 

            for numb, count in counts.items():
                print(f"{numb} appears {count} times")

if __name__ == "__main__":
    main()


