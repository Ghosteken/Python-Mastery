import csv


name = input("Enter your name: ")
age = input("Enter your age: ")
mat_number = input("Enter your matrix number: ")
level = input("Enter your level: ")
city = input("Enter your city: ")
dob = input("Enter your dob: ")

# Specify the CSV file and delimiter
csv_file_path = 'cmp333_user_input.csv'
delimiter = ','  # You can change this to the desired delimiter

# Write user input to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=delimiter)

    
    csv_writer.writerow(['Name', 'Age','mat_number','level', 'City '])

    csv_writer.writerow([name, age,mat_number,level, city])

print(f'User input has been written to the CSV file "{csv_file_path}" with "{delimiter}" as the delimiter.')
