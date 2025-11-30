# Practice 2: The Salary Tax (Logic)
# Goal: Write a function get_salary_details(base_salary) that calculates:
# Tax (10% of base)
# In-hand Salary (Base - Tax)
# Return: Both values.
# Test: Call it with 50000.
def get_salary_details(base_salary):
    tax_rate = 0.10
    tax_amount = base_salary *tax_rate
    in_hand = base_salary - tax_amount
    return in_hand, tax_amount
my_salary, my_tax = get_salary_details(50000)
print(f"In Hand Salary: {my_salary}")
print(f"Taxed Salary: {my_tax}")
