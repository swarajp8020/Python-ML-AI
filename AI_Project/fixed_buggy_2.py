try:
    x = 10 / 0
except ZeroDivisionError:
    x = None # Or handle the error appropriately, e.g., set x to 0, float('inf'), or re-raise a custom error.