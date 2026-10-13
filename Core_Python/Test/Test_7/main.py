from book import Book     

books = {}

while True:
    print("\n -----Book MANAGEMENT SYSTEM -----")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Display Book")
    print("4. Search Book by ID")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        bid = int(input("Enter Book ID: "))

        if bid in books:
            print("Book ID already Exits!")

        else:
            name = input("Enter Book Name: ")
            price = float(input("Enter Book price: "))
            author = input("Enter Author Name: ")

            b = Book(bid, name, price, author)
            books[bid] = b

            print("Book added successfully.")

    elif choice == "2":
        bid = int(input("Enter Book ID to delete:"))

        if bid in books:
            del books[bid]
            print("Book deleted successfully.")

        else:
            print("Book not found.")

    elif choice == "3":
        if not books :
            print("No books available.")

        else:
            for bid, book in books.items():
                print("\n-------")
                book.display()

    elif choice == "4":
        bid = int(input("Enter Book ID to search: "))

        if bid in books:
            print("\n Book Found:")
            books[bid].display()

        else:
            print("Book not found.")

    elif choice =="5":
        print("Existing program...")
        break

    else:
        print("Invalid choice! please try again.")
        
