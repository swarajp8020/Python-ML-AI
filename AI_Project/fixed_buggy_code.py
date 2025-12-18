```python
# Python needs its colons, and the '=' and '+' were socially distancing, causing the total to reset every loop!
def calculate_total(prices):
    total = 0
    for p in prices:
        total += p
    return total

print(calculate_total([10, 20, 30])) # Expected output: 60
```