class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("No books available.")
            return
        print("*** List of Books ***")
        for book in books:
            title, author, release_year, pages = book.strip().split(",")
            print(f"Title: {title}, Author: {author}")

    def add_book(self):
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        pages = input("Enter the number of pages: ")
        book_info = f"{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            if title not in book:
                updated_books.append(book)
            else:
                removed = True
        if not removed:
            print("Book not found.")
            return
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        print("Book removed successfully.")


# Create Library object
lib = Library()

# Menu
while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please choose from 1 to 4.")
