import json
import os

# File for storing book data
LIBRARY_FILE = "library.json"

# Load existing library or create a new one
def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Display menu
def display_menu():
    print("\n📚 Personal Library Manager 📚")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

# Add a book
def add_book(library):
    title = input("Enter the book title: ").strip().title()
    author = input("Enter the author: ").strip().title()
    year = input("Enter the publication year: ").strip()
    genre = input("Enter the genre: ").strip().title()
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": int(year) if year.isdigit() else "Unknown",
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library(library)
    print(f"✅ '{title}' added successfully!")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().title()
    for book in library:
        if book["title"] == title:
            library.remove(book)
            save_library(library)
            print(f"❌ '{title}' removed successfully!")
            return
    print("⚠ Book not found.")

# Search for a book
def search_book(library):
    choice = input("Search by:\n1. Title\n2. Author\nEnter choice: ").strip()
    keyword = input("Enter search keyword: ").strip().title()

    results = [book for book in library if (book["title"] if choice == "1" else book["author"]) == keyword]
    if results:
        print("\n🔎 Search Results:")
        for book in results:
            print(f"- {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '📖 Unread'}")
    else:
        print("⚠ No matching books found.")

# Display all books
def display_books(library):
    if not library:
        print("⚠ No books in your library.")
        return
    print("\n📚 Your Library:")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '📖 Unread'}")

# Display statistics
def display_stats(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books else 0
    print(f"\n📊 Library Stats:\n- Total books: {total_books}\n- Books read: {read_books}\n- Percentage read: {percentage_read:.2f}%")

# Main program loop
def main():
    library = load_library()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            print("📁 Saving library & exiting... Goodbye! 👋")
            save_library(library)
            break
        else:
            print("⚠ Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
