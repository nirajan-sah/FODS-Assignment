import pandas as pd
import numpy as np

BOOKS_FILE = "library_books.csv"

class Library:
    def __init__(self):
        # Define the columns for our DataFrame.
        self.columns = ["Book ID", "Title", "Author", "Is Issued"]
        self.books = self.issue_books()

    def issue_books(self):
        """Loads book details from the CSV file into a pandas DataFrame.
           If the file doesn't exist, an empty DataFrame is created.
        """
        try:
            df = pd.read_csv(BOOKS_FILE)
            # Convert "Is Issued" column to boolean if it exists.
            if "Is Issued" in df.columns:
                df["Is Issued"] = df["Is Issued"].astype(bool)
            print("Books issued successfully.")
            return df
        except FileNotFoundError:
            print("Books file not found. Starting with an empty library.")
            return pd.DataFrame(columns=self.columns)
        except Exception as e:
            print("Error issueing books:", e)
            return pd.DataFrame(columns=self.columns)

    def save_books(self):
        """Saves the current DataFrame of books back to the CSV file."""
        try:
            self.books.to_csv(BOOKS_FILE, index=False)
            print("Books saved successfully.")
        except Exception as e:
            print("Error saving books:", e)

    def add_book(self, book_id, title, author):
        """Adds a new book to the library DataFrame and saves the file."""

        # Check if book_id already exists to avoid duplicates.
        if self.books[self.books["Book ID"] == book_id].empty:
            new_row = pd.DataFrame([[book_id, title, author, False]], columns=self.columns)
            self.books = pd.concat([self.books, new_row], ignore_index=True)
            self.save_books()
            print(f"Book '{title}' added successfully.")
        else:
            print("A book with this ID already exists.")

    def issue_book(self, book_id):
        """Issues a book by setting its 'Is Issued' status to True using numpy."""
        idx = self.books.index[self.books["Book ID"] == book_id].tolist()
        if idx:
            index = idx[0]
            if not self.books.at[index, "Is Issued"]:
                # Using numpy's where to update the status conditionally.
                self.books["Is Issued"] = np.where(self.books["Book ID"] == book_id, True, self.books["Is Issued"])
                self.save_books()
                print(f"Book '{self.books.at[index, 'Title']}' has been issued.")
            else:
                print("This book is already issued.")
        else:
            print("Book ID not found.")

    def return_book(self, book_id):
        """Returns a book by setting its 'Is Issued' status to False using numpy."""
        idx = self.books.index[self.books["Book ID"] == book_id].tolist()
        if idx:
            index = idx[0]
            if self.books.at[index, "Is Issued"]:
                self.books["Is Issued"] = np.where(self.books["Book ID"] == book_id, False, self.books["Is Issued"])
                self.save_books()
                print(f"Book '{self.books.at[index, 'Title']}' has been returned.")
            else:
                print("This book was not issued.")
        else:
            print("Book ID not found.")

    def search_book(self, query):
        """Search for books by title or author using pandas filtering."""
        query = query.lower()
        results = self.books[
            self.books["Title"].str.lower().str.contains(query) |
            self.books["Author"].str.lower().str.contains(query)
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

    # For demonstration, add some default books if the library is empty.
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

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            book_id = input("Enter the Book ID to issue: ")
            library.issue_book(book_id)
        elif choice == "2":
            book_id = input("Enter the Book ID to return: ")
            library.return_book(book_id)
        elif choice == "3":
            query = input("Enter title or author to search: ")
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

if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print("An unexpected error occurred:", e)
