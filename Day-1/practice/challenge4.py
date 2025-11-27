# Task 1: The Shopping Cart (Lists)
# Create an empty list called cart.

# Use a loop to ask the user "Enter item to buy (or type 'done' to finish):".

# Add each item to the list.

# Once the loop breaks, print the total number of items and the first 3 items only (use slicing!).
cart = [] # 1. Create empty list

while True: # 2. Start an infinite loop (Keep going forever...)
    item = input("Enter item to buy (or type 'done' to finish): ")
    
    # 3. Check if we should stop BEFORE adding the item
    if item == "done":
        break # Smash out of the loop immediately!
    
    # 4. If not 'done', add to list
    cart.append(item)

# 5. This runs only after the 'break' happens
print(f"Total items: {len(cart)}") # len() gives the size (like .size() in Java)
print(f"First 3 items: {cart[0:3]}") # Slicing works here