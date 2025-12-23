try:
    x = 10 / 0
except ZeroDivisionError:
    # Handle the division by zero error gracefully.
    # Assigning float('nan') (Not a Number) is a common way to represent
    # the result of an undefined mathematical operation.
    # Alternatively, you could assign None, 0, or raise a custom error.
    x = float('nan')