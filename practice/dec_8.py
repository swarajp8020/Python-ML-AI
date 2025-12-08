inventory = {
    "laptop":12,
    "mouse":5
}
while True:
    print("\nInventory Management System")
    print("1. current stock: ")
    print("2. add/update items: ")
    print("3. delete/remove items: ")
    print("4. Exit from IMS!")
    choice = int("Enter number from 1-4: ")
    if choice == "4":
        print("Goodbye!")
        break
    elif choice == "1":
        print("\nCurrent Stock")
    elif choice == "2":
        name = input("Enter new item name: ")
        try:
            qty = int(input("Enter new item quantity"))
            inventory[name] = qty
            print(f"Success! {name} is now at{qty}")
        except ValueError:
            print("Error: quantity must be number")
