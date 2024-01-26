def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilometers_to_miles(kilometers):
    return kilometers * 0.621371

def kilogram_to_milligrams(kilogram):
    return kilogram * 1e6

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius} Celsius is equal to {celsius_to_fahrenheit(celsius):.2f} Fahrenheit")

    kilometers = float(input("\nEnter distance in kilometers: "))
    print(f"{kilometers} kilometers is equal to {kilometers_to_miles(kilometers):.2f} miles")

    kilogram = float(input("\nEnter weight in kilograms: "))
    print(f"{kilogram} kilograms is equal to {kilogram_to_milligrams(kilogram):.2f} milligrams")

if __name__ == "__main__":
    main()
