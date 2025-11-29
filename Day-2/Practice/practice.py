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
# employees = [
#     {"name": "Amit", "dept": "Sales", "salary": 50000},
#     {"name": "Neha", "dept": "Tech", "salary": 80000},
#     {"name": "Raj", "dept": "Tech", "salary": 82000},
# ]
# total_tech_salary = 0
# for emp in employees:
#     if emp['dept'] == "Tech":
#         print(f"Techie Found {emp['name']}")
#         total_tech_salary += emp['salary']
# print(f'Total Tech Salary {total_tech_salary}')

logs = [
    "ERROR:DB_Connection:Fail",
    "INFO:User_Swaraj:LoginSuccess",
    "WARNING:Disk_Space:Low"
]
log_parser = [log.split(':') for log in logs]
for item in log_parser:
    level=item[0]
    source=item[1]
    message=item[2]
    print(f"[{level}] reported by [{source}:{message}]")