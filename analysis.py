import csv
import json

# Replace 'data.csv' with the actual path to your CSV file.
csv_file = 'dataset.csv'

result = []
seen_combinations = set()

with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for row in csv_reader:
        combination = (
            row['VehicleMake'],
            row['Model'],
            row['ModelYear'],
            row['TecDocNo'],
        )
        if combination not in seen_combinations:
            row_dict = {
                'VehicleMake': row['VehicleMake'],
                'Model': row['Model'],
                'ModelYear': row['ModelYear'],
                'TecDocNo': row['TecDocNo'],
            }
            result.append(row_dict)
            seen_combinations.add(combination)

# Sort the 'result' list based on the 'VehicleMake' key in alphabetical order.
result_sorted = sorted(result, key=lambda x: x['VehicleMake'])

# Replace 'output.json' with the desired file path and name for the JSON file.
output_file = 'output.json'

with open(output_file, 'w') as json_file:
    json.dump(result_sorted, json_file, indent=2)

print(f"JSON data has been written to '{output_file}'.")
