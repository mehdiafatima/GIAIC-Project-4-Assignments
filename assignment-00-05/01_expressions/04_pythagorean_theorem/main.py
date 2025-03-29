import math

def main():

    side_ab = float(input("Enter the length of side AB: "))
    side_bc = float(input("Enter the length of side BC: "))

    side_ac = math.sqrt(side_ab**2 + side_bc**2)
    print("The length of side AC is: ", side_ac)

if __name__ == "__main__":    
    main()