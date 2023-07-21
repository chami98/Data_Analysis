import csv
import json

# Replace 'data.csv' with the actual path to your CSV file.
csv_file = 'dataset.csv'

result = {}
seen_combinations = set()

with open(csv_file, 'r') as file:
    csv_reader = csv.DictReader(file, delimiter=';')
    for row in csv_reader:
        # Strip unwanted spaces from the fields.
        vehicle_make = row['VehicleMake'].strip()
        model = row['Model'].strip()
        model_year = row['ModelYear'].strip()
        tec_doc_no = int(row['TecDocNo'].strip())

        combination = (vehicle_make, model, model_year)
        if combination in seen_combinations:
            if tec_doc_no not in result[combination]['TecDocNo']:
                result[combination]['TecDocNo'].append(tec_doc_no)
        else:
            result[combination] = {
                'VehicleMake': vehicle_make,
                'Model': model,
                'ModelYear': model_year,
                'TecDocNo': [tec_doc_no],  # Initialize TecDocNo as a list with the first value.
            }
            seen_combinations.add(combination)

# Convert the 'result' dictionary values to a list of dictionaries.
result_sorted = list(result.values())

# Sort the 'result_sorted' list based on the 'VehicleMake' key in alphabetical order.
result_sorted.sort(key=lambda x: x['VehicleMake'])

# Replace 'output.json' with the desired file path and name for the JSON file.
output_file = 'output.json'

with open(output_file, 'w') as json_file:
    json.dump(result_sorted, json_file, indent=2)

print(f"JSON data has been written to '{output_file}'.")
