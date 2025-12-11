# buggy_code.py
def calculate_total(prices): # Fix: Added colon after function definition
    total = 0
    for p in prices: # Fix: Added colon after loop definition
        # Fix: Changed 'total =+ p' to 'total += p'.
        # '=+ p' incorrectly assigns the value of p to total in each loop iteration (resetting it).
        # '+= p' correctly accumulates p into total.
        total += p
    return total

print(calculate_total([10, 20, 30]))