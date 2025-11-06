# Library Dictionary
library = {}

# 1. Add a new book
def add_book(book_id, title, author, copies):
    if book_id in library:
        print(f" Book ID '{book_id}' already exists.")
    else:
        library[book_id] = {
            "title": title,
            "author": author,
            "copies": copies
        }
        print(f" Book '{title}' added successfully!")

# 2. Update book availability (borrow or return)
def update_copies(book_id, action):
    if book_id in library:
        if action == "borrow":
            if library[book_id]["copies"] > 0:
                library[book_id]["copies"] -= 1
                print(f" One copy of '{library[book_id]['title']}' borrowed.")
            else:
                print(f" No copies of '{library[book_id]['title']}' available.")
        elif action == "return":
            library[book_id]["copies"] += 1
            print(f" One copy of '{library[book_id]['title']}' returned.")
        else:
            print(" Invalid action. Use 'borrow' or 'return'.")
    else:
        print(f" Book ID '{book_id}' not found.")

# 3. Remove a book
def remove_book(book_id):
    if book_id in library:
        removed_title = library[book_id]["title"]
        del library[book_id]
        print(f" Book '{removed_title}' removed from library.")
    else:
        print(f" Book ID '{book_id}' not found.")

# 4. List all available books
def list_books():
    if library:
        print("\n Available Books:")
        for book_id, details in library.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Copies: {details['copies']}")
    else:
        print(" No books in the library.")

# Sample Execution
add_book("Book001", "Python Programming", "Guido van Rossum", 5)
add_book("Book002", "Data Science Essentials", "Andrew Ng", 3)
update_copies("Book001", "borrow")
update_copies("Book002", "return")
remove_book("Book002")
list_books()
