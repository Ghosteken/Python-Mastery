def multiplication_table(number):
    print(f"Multiplication Table for {number}:")
    i = 1
    while i <= 10:
        result = number * i
        print(f"{number} x {i} = {result}")
        i += 1

def main():
    user_input = int(input("Enter a number to generate its multiplication table: "))
    multiplication_table(user_input)

if __name__ == "__main__":
    main()
