def check_in_range(number, lower_limit, upper_limit):
    return lower_limit <= number <= upper_limit

# Test the function
num_to_check = int(input("Enter a number: "))
lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

if check_in_range(num_to_check, lower_limit, upper_limit):
    print(f"{num_to_check} is within the range [{lower_limit}, {upper_limit}]")
else:
    print(f"{num_to_check} is outside the range [{lower_limit}, {upper_limit}]")
