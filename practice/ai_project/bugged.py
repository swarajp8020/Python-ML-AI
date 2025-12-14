def calculate_total(prices)
    total = 0
    for p in prices
        total =+ p  # Syntax error and logic error!
    return total

print(calculate_total([10, 20, 30]))