# 1. The Database (Just a dictionary)
# Key = Item Name (String)
# Value = Stock Count (Int)
inventory = {
    "Laptop":10,
    "Mouse":12,
    "Keyboard":4
}
while True:
    print("\n--- INVENTORY MANAGER ---")
    print("1. View Stock")
    print("2. Add/Update Item")
    print("3. Delete Item")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "4":
        print("Goodbye!")
        break
    elif choice == "1":
        print("\nCurrent Stock")
    # ADD/UPDATE LOGIC
    elif choice == "2":
        name = input("Enter Item Name: ")
        
        # Crash protection: Ensure quantity is a number
        try:
            qty = int(input("Enter Quantity: "))
            
            # THE MAGIC LINE
            # No .put(), no setters. Just direct assignment.
            inventory[name] = qty
            
            print(f"Success! {name} is now at {qty}.")
            
        except ValueError:
            print("Error: Quantity must be a number!")
    elif choice == "3":
        name = input("Enter item to remove: ")
        if name in inventory:
            inventory.pop(name)
        else:
            print("Item not found!")

        for item, count in inventory.items():
            print(f"-{item}:{count}")