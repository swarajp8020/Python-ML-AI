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

        for item, count in inventory.items():
            print(f"-{item}:{count}")