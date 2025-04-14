import pandas as pd
'''
A simple library system
'''
BOOKS_FILE = "library_books.csv"

class Library:
    def __init__(self):
        self.columns = ["Book ID", "Title", "Author", "Is Issued"]
        self.books = self.load_books()

    def load_books(self):
        """Loads book details from the CSV file into a pandas DataFrame.
           If the file doesn't exist, an empty DataFrame is created.
        """
        try:
            df = pd.read_csv(BOOKS_FILE)
            if "Is Issued" in df.columns:
                df["Is Issued"] = df["Is Issued"].astype(bool)
            print("Books loaded successfully.")
            return df
        except FileNotFoundError:
            print("Books file not found. Starting with an empty library.")
            return pd.DataFrame(columns=self.columns)
        except Exception as e:
            print("Error loading books:", str(e))
            return pd.DataFrame(columns=self.columns)

    def save_books(self):
        """Saves the current DataFrame of books back to the CSV file."""
        try:
            self.books.to_csv(BOOKS_FILE, index=False)
            print("Books saved successfully.")
        except Exception as e:
            print("Error saving books:", str(e))

    def add_book(self, book_id, title, author):
        """Add a new book if the ID is not already in the library."""
        book_id = str(book_id).strip()
        title = title.strip()
        author = author.strip()

        if book_id in self.books["Book ID"].values:
            print("A book with this ID already exists.")
            return

        new_book = {"Book ID": book_id, "Title": title, "Author": author, "Is Issued": False}
        self.books = pd.concat([self.books, pd.DataFrame([new_book])], ignore_index=True)
        self.save_books()
        print(f"Book '{title}' added successfully.")

    def issue_book(self, book_id):
        """Issues a book by setting its 'Is Issued' status to True."""
        book_id = str(book_id).strip()
        mask = self.books["Book ID"] == book_id

        if mask.any():
            if not self.books.loc[mask, "Is Issued"].values[0]:
                self.books.loc[mask, "Is Issued"] = True
                self.save_books()
                title = self.books.loc[mask, "Title"].values[0]
                print(f"Book '{title}' has been issued.")
            else:
                print("This book is already issued.")
        else:
            print("Book ID not found.")

    def return_book(self, book_id):
        """Returns a book by setting its 'Is Issued' status to False."""
        book_id = str(book_id).strip()
        mask = self.books["Book ID"] == book_id

        if mask.any():
            if self.books.loc[mask, "Is Issued"].values[0]:
                self.books.loc[mask, "Is Issued"] = False
                self.save_books()
                title = self.books.loc[mask, "Title"].values[0]
                print(f"Book '{title}' has been returned.")
            else:
                print("This book was not issued.")
        else:
            print("Book ID not found.")

    def search_book(self, query):
        """Search for books by title or author using pandas filtering."""
        query = query.lower().strip()
        results = self.books[
            self.books["Title"].str.lower().str.contains(query, na=False) |
            self.books["Author"].str.lower().str.contains(query, na=False)
        ]
        return results

    def list_books(self):
        """Prints all the books in the library."""
        if self.books.empty:
            print("No books in the library.")
        else:
            print("\nLibrary Books:")
            print(self.books.to_string(index=False))


def main_menu():
    library = Library()

    # Add some default books if the library is empty.
    if library.books.empty:
        library.add_book("1", "The Great Gatsby", "F. Scott Fitzgerald")
        library.add_book("2", "1984", "George Orwell")
        library.add_book("3", "To Kill a Mockingbird", "Harper Lee")

    while True:
        print("\nLibrary Management Menu:")
        print("1. Issue a Book")
        print("2. Return a Book")
        print("3. Search for a Book")
        print("4. List all Books")
        print("5. Add a Book")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            book_id = input("Enter the Book ID to issue: ").strip()
            library.issue_book(book_id)
        elif choice == "2":
            book_id = input("Enter the Book ID to return: ").strip()
            library.return_book(book_id)
        elif choice == "3":
            query = input("Enter title or author to search: ").strip()
            results = library.search_book(query)
            if not results.empty:
                print("\nSearch Results:")
                print(results.to_string(index=False))
            else:
                print("No books found matching the query.")
        elif choice == "4":
            library.list_books()
        elif choice == "5":
            book_id = input("Enter the new Book ID: ")
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            library.add_book(book_id, title, author)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select from the menu.")


main_menu()
