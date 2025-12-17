The original code has a few issues:

1.  **Missing colons (`:`):** Both the function definition (`def calculate_total(prices)`) and the `for` loop (`for p in prices`) are missing the required colon at the end of the line, which causes a `SyntaxError`.
2.  **Incorrect assignment operator (`=+`):** The line `total =+ p` is syntactically valid in Python, but it means "assign the positive value of `p` to `total`." It **does not** mean "add `p` to `total` and store the result in `total`." This causes a logic error where the total will just be the value of the last price, or the last price's positive value (if it were negative). The correct operator for accumulation is `+=`.

Here is the fixed code with a funny explanation of the bug:

```python
# fixed_code.py
def calculate_total(prices):
    total = 0
    for p in prices:
        # Bug fix: '=' and '+' were having an awkward conversation and swapped places.
        # 'total =+ p' means 'total is now positive p,' which is terrible for accounting.
        # We need the accumulation operator: '+='.
        total += p
    return total

print(calculate_total([10, 20, 30]))
```