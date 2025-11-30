# Defined using 'def'
# def greet_user(name):
#     # Logic is indented
#     message = f"Hello, {name}! Welcome to AI Engineering."
#     return message

# # Usage (Outside the indentation)
# print(greet_user("Swaraj"))
# print(greet_user("Google"))

# 'tax_rate' defaults to 0.10 (10%) if the user doesn't provide it
def calculate_salary(base, tax_rate=0.10):
    tax = base * tax_rate
    net_salary = base - tax
    return net_salary

# Scenario 1: Use default tax (10%)
s1 = calculate_salary(100000) 
print(f"Standard Salary: {s1}")

# Scenario 2: Custom tax (30%)
s2 = calculate_salary(100000, 0.30)
print(f"Taxed Salary: {s2}")
