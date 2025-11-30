# Goal: Write a function calculate(a, b) that returns two values: the sum (a+b) and the product (a*b).
# Test: Call it with 5, 10 and print both results.

def calculate(a,b):
    sum = a+b
    product= a*b
    return sum, product
addition, multiplication = calculate(5,10)
print(f"Sum is {addition}")
print(f"prouct is {multiplication}")