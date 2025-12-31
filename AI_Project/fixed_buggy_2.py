try:
    x = 10 / 0
except ZeroDivisionError:
    x = None  # Handle the error by assigning a default value, or log it, or raise a different exception