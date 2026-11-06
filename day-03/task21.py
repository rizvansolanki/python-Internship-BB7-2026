employees = {
    "Rizvan": 25000,
    "samad": 50000,
    "tahir": 40000,
    "Sahil": 60000,
    "arsh": 35000
}

# Sorting by salary in descending order
sorted_employees = sorted(employees.items(), key=lambda x: x[1], reverse=True)

print("Top 3 Highest Paid Employees:")

for name, salary in sorted_employees[:3]:
    print(name, ":", salary)