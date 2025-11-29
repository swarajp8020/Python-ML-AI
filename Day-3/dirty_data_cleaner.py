# Challenge 2: The "Dirty Data Cleaner" This is a test of your List Comprehension memory from yesterday.
# Data:
# raw_prices = [100, -50, 200, None, 50, -10, 300]
# Task: Write a one-line list comprehension that:
# Removes None.
# Removes negative numbers (price > 0).
# Adds 10% tax (multiplies by 1.1) to the remaining numbers.
# Hint: [ price * 1.1 for price in raw_prices if ... and ... ]
raw_prices = [100, -50, 200, None, 50, -10, 300]

# 1. Start with the loop: 'for price in raw_prices'
# 2. Add the Filters (The IF part): 'if price is not None and price > 0'
# 3. Add the Math (The Start): 'price * 1.1'

clean_prices = [price * 1.1 for price in raw_prices if price is not None and price > 0]

print(clean_prices)

# Output will be: [110.0, 220.0, 55.0, 330.0]