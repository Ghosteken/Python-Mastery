import csv

student_data = []
for i in range(10):
    name = input(f'Enter name for student {i+1}: ')
    age = input(f'Enter age for student {i+1}: ')
    mat_number = input(f'Enter matrix number for student {i+1}: ')
    level = input(f'Enter level for student {i+1}: ')
    city = input(f'Enter city for student {i+1}: ')
    dob = input(f'Enter dob for student {i+1}: ')
    student_data.append([name, age, mat_number, level, city])

csv_file_path = 'cmp333_user_input.csv'
delimiter = ','

with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=delimiter)
    csv_writer.writerow(['Name', 'Age', 'mat_number', 'level', 'City'])
    csv_writer.writerows(student_data)

print(f'User input has been written to the CSV file "{csv_file_path}" with "{delimiter}" as the delimiter.')