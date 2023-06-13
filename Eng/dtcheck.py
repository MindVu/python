import csv

filename = "dataset.csv"

def check_csv_for_value_error(filename):
    line_number = 0
    count = 0
    with open(filename, "r") as csv_file:
        reader = csv.reader(csv_file)
        
        for row in reader:
            line_number += 1
            
            try:
                # Attempt to convert each value in the row to float
                _ = [float(value) for value in row]
            except ValueError as e:
                print(f"ValueError occurred in line {line_number}: {e}")
                count += 1
    print(count)
                
check_csv_for_value_error(filename)
