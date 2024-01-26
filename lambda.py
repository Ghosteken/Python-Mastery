# Using lambda function to create an anonymous function
power_of_2 = lambda x: 2 ** x

def display_powers_of_2(n):
    for i in range(n):
        result = power_of_2(i)
        print(f"2^{i} = {result}")

def main():
    n = int(input("Enter the number of powers of 2 to display: "))
    display_powers_of_2(n)

if __name__ == "__main__":
    main()
