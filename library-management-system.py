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
        book_number = 1
        for book in books:
            book_data = book.strip().split(",")
            if len(book_data) < 5:  # Ensure the book has at least 5 values
                print("Error: Invalid book data format.")
                continue
            book_id, title, author, release_year, pages = book_data[:5]
            print(f"Book {book_number}\n-------\nID: {book_id}\nTitle: {title}, Author: {author} \nYear: {release_year}, {pages} Pages")
            book_number += 1
            if book_number <= len(books):  # Print separator for all books except the last one
                print("------------------------------------")



    def add_book(self):
        book_id = input("Enter the ID of the book: ")
        
        # Check if the entered book_id already exists
        if self.check_id_existence(book_id):
            print("Book ID already exists. Please choose a different ID.")
            return

        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        release_year = input("Enter the release year of the book: ")
        pages = input("Enter the number of pages: ")
        book_info = f"{book_id},{title},{author},{release_year},{pages}\n"
        self.file.write(book_info)
        print(f"Book '{title}' added successfully.")

    def check_id_existence(self, book_id):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            if book.startswith(book_id + ','):
                return True
        return False


    def remove_book(self):
        remove_id = input("Enter the ID of the book to remove: ")
        remove_title = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            book_data = book.strip().split(",")
            book_id, title, author, release_year, pages = book_data[:5]
            if book_id == remove_id and title == remove_title:
                removed = True
                removed_title = title  # Store the title of the removed book for use in the print section
            else:
                updated_books.append(book)
        if not removed:
            print("Book not found.")
            return
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        print(f"Book '{removed_title}' removed successfully.")




# Create Library object
library = Library()

# Menu Section
while True:
    print("\n*** MENU ***")
    print("1) List Books ---> list")
    print("2) Add Book ---> add")
    print("3) Remove Book ---> remove")
    print("4) Exit ---> exit")

    choice = input("Enter your command: ")

    if choice.lower() == 'list':
        library.list_books()
    elif choice.lower() == 'add':
        library.add_book()
    elif choice.lower() == 'remove':
        library.remove_book()
    elif choice.lower() == 'exit':
        break
    else:
        print("Invalid command. Please type valid command.")
