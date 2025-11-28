# numbers = [2,4,3,6,2]
# # evens = [n for n in numbers if n%2==0]
# # print(evens)
# doubled =[n*2 for n in numbers]
# print(doubled)

# Pattern 1: The "Transformer" (Change everything)
# Use this when you want to modify every single item.

# Formula: [ MODIFY(item) for item in list ]
# names = ["Swaraj","sahil"]
# capitalized = [name.upper() for name in names]
# print(capitalized)

# Pattern 2: The "Filter" (Pick specific things)
# Use this when you want to keep the data same, but remove the bad ones.
# Formula: [ item for item in list if CONDITION ]
# scores = [10,20,40,50,95,100]
# updated = [score for score in scores if score > 40 ]
# print(updated)

# Pattern 3:The "Combo" (Google Level)
# Use this to Filter AND Transform at the same time.

# Formula: [ MODIFY(item) for item in list if CONDITION ]
# employees = [
#     {"name": "Amit", "dept": "Sales"},
#     {"name": "Neha", "dept": "Tech"},
#     {"name": "Raj", "dept": "Tech"},
# ]
# # "Give me the NAME for every emp in employees if DEPT is Tech"
# tech_names = [emp['name'] for emp in employees if emp['dept']=="Tech"]
# print(tech_names)

files = ["report.pdf", "script.py", "image.png", "data.csv", "logic.py"]

python_file_only = [file.upper() for file in files if file.endswith(".py")==True]
print(python_file_only)

