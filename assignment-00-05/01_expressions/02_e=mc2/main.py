C = 299792458

def main():
    
    mass = float(input("Enter kilos of mass: "))

    energy = mass *C**2


    print("e = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {C} m/s")
    print(f"{energy} joules of energy!")

if __name__ == "__main__":
    main()


