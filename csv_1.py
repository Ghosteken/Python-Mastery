import csv

# Sample data
data = [
    ['Name', 'Age', 'City'],
    ['John Doe', 30, 'New York'],
    ['Jane Smith', 25, 'Los Angeles'],
    ['Bob Johnson', 35, 'Chicago']
]

# Specify the CSV file and delimiter
csv_file_path = 'example.csv'
delimiter = ';'  # You can change this to the desired delimiter (e.g., ',' for a standard CSV file)

# Write data to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=delimiter)

    #  header
    csv_writer.writerow(data[0])

    #  data rows
    csv_writer.writerows(data[1:])

print(f'CSV file "{csv_file_path}" has been created with "{delimiter}" as the delimiter.')
