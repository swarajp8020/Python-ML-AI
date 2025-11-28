# Task 3: The "Mini-Database" (List of Dicts) This is exactly how data looks when you fetch it from an API.
# Create a list of dictionaries representing employees:
# Python
# employees = [
#     {"name": "Amit", "dept": "Sales", "salary": 50000},
#     {"name": "Neha", "dept": "Tech", "salary": 80000},
#     {"name": "Raj", "dept": "Tech", "salary": 82000},
# ]
# Your Goal:
# Loop through this list.
# Calculate the Total Salary of everyone in the "Tech" department.
# Print the total.
employees = [
    {"name": "Amit", "dept": "Sales", "salary": 50000},
    {"name": "Neha", "dept": "Tech", "salary": 80000},
    {"name": "Raj", "dept": "Tech", "salary": 82000},
]
total_tech_salary = 0
for emp in employees:
    if emp['dept'] == "Tech":
        print(f"Found Techie {emp['salary']}")
        total_tech_salary += emp["salary"]
print(f"Total Tech Salary {total_tech_salary}")