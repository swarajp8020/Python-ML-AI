# 1. Create the Dictionary
books = {
    "Harry Potter": "Available",
    "Lord of the Rings": "Available",
    "Dune": "Borrowed"
}

while True:
    print("\n--- LIBRARY SYSTEM ---")
    print("1. View Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "5":
        print("Goodbye!")
        break
        
    elif choice == "1":
        print("\n--- Book List ---")
        # CHALLENGE 1: Loop through books and print "Book: Status"
        # CODE HERE (2 lines)
        for key, value in books.items():
            print(f"{key}:{value}")
        
    elif choice == "2":
        name = input("Enter Book Name: ")
        # CHALLENGE 2: Add the book to the dictionary with status "Available"
        # CODE HERE (1 line)
        books[name] = "Available"
        print("Book Added!")
        
    elif choice == "3":
        name = input("Which book to borrow? ")
        # CHALLENGE 3: Check if book exists. If yes, change value to "Borrowed"
        if name in books:
            # CODE HERE (1 line)
            books[name] = "Borrowed"
            print("Enjoy reading!")
        else:
            print("Book not found.")

    elif choice == "4":
        name = input("Which book to return? ")
        # CHALLENGE 4: Check if book exists. If yes, change value to "Available"
        if name in books:
            # CODE HERE (1 line)
            books[name] = "Available"
            print("Thanks for returning!")
        else:
            print("Book not found.")