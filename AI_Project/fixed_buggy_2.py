try:
    x = 10 / 0
except ZeroDivisionError:
    x = float('nan') # Assign NaN (Not a Number) as the result of an undefined operation, preventing a crash.
