def calculate_amount_payable(total_amount):
    if total_amount >= 100000:
        discount = 0.2
    elif 50000 <= total_amount < 100000:
        discount = 0.1
    elif 10000 <= total_amount < 50000:
        discount = 0.02
    else:
        discount = 0
    
    amount_payable = total_amount - (total_amount * discount)
    return amount_payable

def main():
    total_amount = float(input("Enter the total amount of goods: "))
    amount_payable = calculate_amount_payable(total_amount)
    print(f"The amount payable after discount is: {amount_payable:.2f}")

if __name__ == "__main__":
    main()
