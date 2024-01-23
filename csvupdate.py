import csv

csv_file_path = 'cmp333_user_input.csv'
delimiter = ','

# Read existing data from the CSV file
existing_data = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=delimiter)
    existing_data = list(csv_reader)

new_name = input("Enter a new name: ")
new_age = input("Enter a new age: ")
new_city = input("Enter a new city: ")
new_level = input("Enter a new level: ")
new_mat_number = input("Enter a new matrix number: ")
dob = input("dob: ")

new_row = [new_name, new_age, new_city, new_level, new_mat_number]
existing_data.append(new_row)

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=delimiter)
    
    csv_writer.writerows(existing_data)

print(f'New data has been added to the CSV file "{csv_file_path}" with "{delimiter}" as the delimiter.')
