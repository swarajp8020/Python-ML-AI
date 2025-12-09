inventory = {
    "Laptop":12,
    "mouse":12,
    "KeyBoard":3
}
while True:
    print("\nInventory Management System")
    print("1. current stock")
    print("2. add/update")
    print("3. delete/remove")
    print("4. Exit from Inventory Management System")
    choice = input("Enter IMS numbers 1-4: ")
    if choice == "4":
        print("Goodbye!")
        break
    elif choice == "1":
        print("\ncurrent status")

        for item, count in inventory.items():
            print(f"-{item}:{count}")
    elif choice == "2":
        name = input("Enter Item name: ")
        try:
            qty = int(input("Enter quantity: "))
            inventory[name] =qty
            print(f"Success! {name} is now at {qty}")
        except ValueError:
            print("Error! quantity must be number!")
    elif choice == "3":
        name = input("Enter Item name wants to remove: ")
        if name in inventory:
            inventory.pop(name)
        else:
            print("Item not found!")
       
    