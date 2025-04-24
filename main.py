import json
import os  # File handling

library_file_path = "library.txt"

# Load existing library data from file
def load_library_data():
    if os.path.exists(library_file_path):
        with open(library_file_path, "r") as file:
            return json.load(file)
    return []

# Save library data to file
def save_library_data(library_records):
    with open(library_file_path, "w") as file:
        json.dump(library_records, file, indent=4)

# Add a new book
def add_new_book(library_records):
    print("\n--- Add a New Book ---")
    book_title = input("Book Title: ")
    book_author = input("Author: ")
    publication_year = input("Publication Year: ")
    book_genre = input("Genre: ")
    is_read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    new_book = {
        "title": book_title,
        "author": book_author,
        "year": publication_year,
        "genre": book_genre,
        "read": is_read
    }

    library_records.append(new_book)
    save_library_data(library_records)
    print(f"✅ Book '{book_title}' has been added to your library.")

# Remove a book by title
def delete_book_by_title(library_records):
    print("\n--- Remove a Book ---")
    title_to_remove = input("Enter the title of the book to remove: ").strip()
    original_length = len(library_records)

    updated_library = [book for book in library_records if book["title"].lower() != title_to_remove.lower()]
    
    if len(updated_library) < original_length:
        save_library_data(updated_library)
        print(f"🗑️ Book '{title_to_remove}' has been removed.")
        return updated_library
    else:
        print(f"❌ Book '{title_to_remove}' not found.")
        return library_records

# Search for a book by title
def find_book_by_title(library_records):
    print("\n--- Search for a Book ---")
    search_title = input("Enter the title to search: ").strip()
    matched_books = [book for book in library_records if book["title"].lower() == search_title.lower()]
    
    if matched_books:
        print(f"\n📚 Found {len(matched_books)} result(s):")
        for book in matched_books:
            print(f"""
🔸 Title : {book['title']}
🔸 Author: {book['author']}
🔸 Year  : {book['year']}
🔸 Genre : {book['genre']}
🔸 Read  : {'Yes' if book['read'] else 'No'}
----------------------------""")
    else:
        print(f"❌ No book with the title '{search_title}' found.")

# Show all books
def show_all_books(library_records):
    print("\n--- All Books in Your Library ---")
    if library_records:
        for index, book in enumerate(library_records, start=1):
            print(f"""
📘 Book #{index}
🔸 Title : {book['title']}
🔸 Author: {book['author']}
🔸 Year  : {book['year']}
🔸 Genre : {book['genre']}
🔸 Read  : {'Yes' if book['read'] else 'No'}
----------------------------""")
    else:
        print("📂 Your library is currently empty.")

# Show reading statistics
def display_reading_stats(library_records):
    total_books = len(library_records)
    read_books = sum(1 for book in library_records if book["read"])
    read_percentage = (read_books / total_books * 100) if total_books > 0 else 0
    
    print("\n📊 --- Library Statistics ---")
    print(f"Total Books     : {total_books}")
    print(f"Books Read      : {read_books}")
    print(f"Read Percentage : {read_percentage:.2f}%")

# Mark a book as read
def mark_book_as_read(library_records):
    print("\n--- Mark a Book as Read ---")
    book_title = input("Enter the title of the book: ").strip()
    
    for book in library_records:
        if book["title"].lower() == book_title.lower():
            book["read"] = True
            save_library_data(library_records)
            print(f"📗 Book '{book_title}' marked as read.")
            return
    print(f"❌ Book '{book_title}' not found.")

# Mark a book as unread
def mark_book_as_unread(library_records):
    print("\n--- Mark a Book as Unread ---")
    book_title = input("Enter the title of the book: ").strip()
    
    for book in library_records:
        if book["title"].lower() == book_title.lower():
            book["read"] = False
            save_library_data(library_records)
            print(f"📕 Book '{book_title}' marked as unread.")
            return
    print(f"❌ Book '{book_title}' not found.")

# Display menu and interact
def main():
    library_records = load_library_data()
    while True:
        print("""
=============================
📚 PERSONAL LIBRARY MENU
=============================
1. ➕ Add Book
2. 🗑️  Remove Book
3. 🔍 Search Book
4. 📖 Display All Books
5. 📊 View Statistics
6. ✅ Mark Book as Read
7. ❌ Mark Book as Unread
8. 🚪 Exit
""")
        user_choice = input("Choose an option (1-8): ").strip()
        
        if user_choice == "1":
            add_new_book(library_records)
        elif user_choice == "2":
            library_records = delete_book_by_title(library_records)
        elif user_choice == "3":
            find_book_by_title(library_records)
        elif user_choice == "4":
            show_all_books(library_records)
        elif user_choice == "5":
            display_reading_stats(library_records)
        elif user_choice == "6":
            mark_book_as_read(library_records)
        elif user_choice == "7":
            mark_book_as_unread(library_records)
        elif user_choice == "8":
            print("\n📚 Exiting the library system. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()
