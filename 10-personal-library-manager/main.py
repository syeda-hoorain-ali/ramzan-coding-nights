import json

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials."""

    def __init__(self):
        """Initialize a new book collection with an empty list and set up file storage."""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()


    def read_from_file(self):
        """Load saved books from a JSON file into memory.  
        If the file doesn't exist or is corrupted, start with an empty collection."""

        try:
            with open(self.storage_file, 'r') as file:
                self.book_list = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []
            
    
    def save_to_file(self):
        """Store the current book collection to a JSON file for permenant storage."""

        with open(self.storage_file, 'w') as file:
            json.dump(self.book_list, file, indent=4)


    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user."""

        title = input("\nEnter book title: ").strip()
        author = input("Enter author name: ").strip()
        publication_year = input("Enter publication year: ").strip()

        while not publication_year.isdigit():
            publication_year = input("Enter a valid publication year: ").strip()

        genre = input("Enter genre: ").strip()
        is_book_read = input("Have you read this book? (yes/no) ").strip().lower() in ['yes', 'y']

        new_book = {
            "title": title,
            "author": author,
            "publication_year": int(publication_year),
            "genre": genre,
            "is_readed": is_book_read
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("Book added successfully!\n")


    def delete_book(self):
        """Remove a book from the collection using its title."""
        book_title = input("\nEnter the title of the book to remove: ").strip()

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                print("Book removed successfully!\n")
                return
        
        print("Book not found!\n")


    def find_book(self):
        """Search for books in the collection by title or author name."""
        input("\nSearch by:\n1. Title\n2. Author\nEnter your choice: ")
        search_text = input("\nEnter search term: ").strip().lower()
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower()
            or search_text in book["author"].lower()
        ]

        if found_books:
            print("\nMatching books.")

            for i, book in enumerate(found_books, 1):
                reading_status = "Read" if book["is_readed"] else "Unread"
                print(f"{i}. {book["title"].capitalize()} by {book["author"].capitalize()} ({book["publication_year"]}) - {book["genre"].capitalize()} - {reading_status}")
            print()

        else:
            print("\nNo matching books found. \n")


    def update_book(self):
        """Modify the details of an existing book in the collection"""
        
        book_title = input("\nEnter the title of the book you want to edit: ")

        for book in self.book_list:
            if book["title"].lower() == book_title.strip().lower():
                print("\nLeave blank to keep existing value.")        

                book["title"] = input(f"Title ({book['title']}): ").strip() or book["title"]
                book["author"] = input(f"Author name ({book['author']}): ").strip() or book["author"]
                
                # book_year = str(book['publication_year'])
                # publication_year = input(f"Publication year ({book_year}): ").strip() or book_year
                # while not publication_year.isdigit():
                #     publication_year = input(f"Enter a valid publication year ({book_year}): ").strip() or book_year
                # book["publication_year"] = int(publication_year)

                publication_year = input(f"Publication year ({book['publication_year']}): ").strip()
                book["publication_year"] = int(publication_year) if publication_year.isdigit() else book["publication_year"]

                book["genre"] = input(f"Genre ({book['genre']}): ").strip() or book["genre"]
                book["is_readed"] = input(f"Have you read this book? (yes/no): ").strip().lower() in ['yes', 'y']

                self.save_to_file()
                print("\nBook updated successfully!\n")
                return
        print("Book not found!\n")
    

    def show_all_books(self):
        """Display all books in the collection with their details."""
        
        if not self.book_list:
            print("\nYour collection is empty.\n")
            return
        
        print("\nYour Book Collection:")
        for i, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["is_readed"] else "Unread"
            print(f"{i}. {book["title"].capitalize()} by {book["author"].capitalize()} ({book["publication_year"]}) - {book["genre"].capitalize()} - {reading_status}")

        print()


    def show_reading_progress(self):
        """Calculate and display statistics about you rerading progress."""

        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book['is_readed'])
        completion_rate = (completed_books / total_books * 100) if total_books > 0 else 0

        print(f"\nTotal books in collection: {total_books}")
        print(f"Reading progress: {completion_rate:.2f}%\n")


    def start_application(self):
        """Run the main application loop with a user-friendly menu interface."""

        while True:
            print("📚 Welcome to your book collection manager! 📚")
            print('----------------------------------------------')
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")


            user_choice = input("Please choose an option (1-7): ").strip()

            if user_choice == '1':
                self.create_new_book()
            
            elif user_choice == '2':
                self.delete_book()

            elif user_choice == '3':
                self.find_book()

            elif user_choice == '4':
                self.update_book()

            elif user_choice == '5':
                self.show_all_books()

            elif user_choice == '6':
                self.show_reading_progress()

            elif user_choice == '7':
                self.save_to_file()
                print("\nThank you for using book collection manager. Goodbye!\n")
                break

            else:
                print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    try:
        book_manager = BookCollection()
        book_manager.start_application()
    except KeyboardInterrupt:
        print("\nThank you for using book collection manager. Goodbye!\n")
