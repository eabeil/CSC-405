import csv

with open('insurance.csv') as file:
    reader = csv.DictReader(file)

    columns = reader.fieldnames
    rows = list(reader)


# part two printing number of records and column names

print(f"Number of records: {len(rows)}")
print(f"Columns: {columns}")

# part three computing stats

# part a average of age columns


sum_age = 0

for row in rows:
    sum_age += float(row['age'])

average_age = sum_age / len(rows)

print(f"Average age: {average_age:.2f}")

# part b count record for each gender

gender_count = {}

for row in rows:
    gender = row['sex']
    if gender not in gender_count:
        gender_count[gender] = 0

    gender_count[gender] += 1

    print ('Gender count: ', gender_count)

    for gender, count in gender_count.items():
        print(f"{gender}: {count}")


# part c 


gender_age_sum = {}
gender_age_count = {}

for row in rows:
    gender = row['sex']
    age = float(row['age'])

    if gender not in gender_age_sum:
        gender_age_sum[gender] = 0
        gender_age_count[gender] = 0


    gender_age_sum[gender] += age
    gender_age_count[gender] += 1



    for gender, total_age in gender_age_sum.items():
        average_age = total_age / gender_age_count[gender]
        print(f"{gender} Average age = {average_age:.2f}")
        

