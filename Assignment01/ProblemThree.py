import csv

with open('insurance.csv') as file:
    reader = csv.DictReader(file)

    columns = reader.fieldnames
    rows = list(reader)


# part two printing number of records and column names

print(f"Number of records: {len(rows)}")
print(f"Columns: {columns}")
